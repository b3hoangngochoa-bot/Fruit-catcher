from Models.base_entity import BaseEntity


class Basket(BaseEntity):
    def __init__(self, width=100, height=50, image=None):
        super().__init__(width=width, height=height, image=image, tag="BASKET")
        self.color = (139, 69, 19)

    def update(self, input_data):
        if not self.active:
            return

        basket = input_data.get("basket", {})
        self.x = basket.get("x") or self.x
        self.y = basket.get("y") or self.y

    def get_render_data(self):
        if not self.active:
            return None

        return {
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "color": self.color,
            "radius": None,
            "layer": self.render_layer,
            "shape": "rect",
            "basket": True,
            "image": self.image or None,
        }
