from .ui_element import UIElement
from Core.event_type import EventType
import pygame


class Button(UIElement):
    def __init__(
        self,
        x,
        y,
        width=100,
        height=50,
        text: str = "",
        image=None,
        color=None,
        action: EventType = None,
    ):
        super().__init__(x=x, y=y, width=width, height=height, image=image)
        self.font = pygame.font.SysFont("Arial", 24)
        self.text_surface = self.font.render(text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=(self.x, self.y))
        self.color = color
        self.action = action
        self.hover_time = 0

    def update(self, event_bus, cursor):
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
