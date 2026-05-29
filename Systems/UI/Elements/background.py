from .ui_element import UIElement
from Systems.Render.render_layer import RenderLayer


class Background(UIElement):
    def __init__(
        self,
        x=0,
        y=0,
        width=100,
        height=50,
        image=None,
        color=None,
        full_screen: bool = True,
    ):
        super().__init__(x=x, y=y, width=width, height=height, image=image)
        self.color = color
        self.render_layer = RenderLayer.BACKGROUND
        self.full_screen = full_screen  # Indicates this should cover the entire screen

    def update(self, event_bus, cursor, delta_time):
        return None

    def get_render_data(self):
        if not self.enabled:
            return None

        return {
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "color": self.color,
            "layer": self.render_layer,
            "image": self.image or None,
            "full_screen": self.full_screen,
        }
