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
        self.current_color = color
        self.action = action
        self.hover_time = 0
        self.hover_threshold = 1.0  # seconds to trigger hold action

    def update(self, input_data, event_bus, cursor, delta_time):
        """
        Detect hover / hold → return Event
        """
        cursor.update(input_data)
        self.hover_time += delta_time
        if self._is_hovered(cursor):
            self.current_color = (200, 200, 200)  # lighter color on hover
            if self.hover_time >= self.hover_threshold:
                event_bus.emit(self.action, {})  # emit event with empty payload
                self.hover_time = 0  # reset hover time after action
        else:
            self.hover_time = 0  # reset if not hovered
            self.current_color = self.color  # reset to original color
        return None
    
    def _is_hovered(self, cursor):
        return (
            self.x - self.width / 2 <= cursor.x <= self.x + self.width / 2
            and self.y - self.height / 2 <= cursor.y <= self.y + self.height / 2
        )

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
            "color": self.current_color,
            "radius": None,
            "layer": self.render_layer,
            "shape": "rect",
            "image": self.image or None,
        }
