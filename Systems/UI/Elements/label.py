from .ui_element import UIElement
from Core.event_type import EventType
import pygame


class Label(UIElement):
    def __init__(
        self,
        x,
        y,
        size: int,
        text: str = "",
        color=None,
    ):
        super().__init__(x=x, y=y)
        self.size = size
        self.font = pygame.font.SysFont("Arial", self.size)
        self.color = color or (255, 255, 255)
        self.text_surface = self.font.render(text, True, self.color)
        self.text_rect = (self.x, self.y)

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
            "text_surface": self.text_surface,
            "text_rect": self.text_rect,
            "color": self.color,
            "layer": self.render_layer,
        }
