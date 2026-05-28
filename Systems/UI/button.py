from UI.ui_element import UIElement


class Button(UIElement):
    def __init__(
        self,
        x,
        y,
        width=100,
        height=50,
        text_surface=None,
        text_rect=None,
        image=None,
        color=None,
        action=None,
    ):
        super().__init__(x=x, y=y, width=width, height=height, image=image)
        self.text_surface = text_surface
        self.text_rect = text_rect
        self.color = color
        self.action = action
        self.hover_time = 0

    def update(self, cursor):
        """
        Detect hover / hold → return Event
        """
        return None

    def get_render_data(self):
        if not self.visible:
            return None
        
        return {
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "text_surface": self.text_surface,
            "text_rect": self.text_rect,
            "color": self.color,
            "radius": None,
            "layer": self.render_layer,
            "shape": "rect",
            "image": self.image or None,
        }
