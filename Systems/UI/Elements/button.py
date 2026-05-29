import pygame
from .ui_element import UIElement
from Core.event_type import EventType
from Utils import load_asset, constants

load_ui_image = load_asset.load_ui_image


class Button(UIElement):
    def __init__(
        self,
        x,
        y,
        width=100,
        height=50,
        text: str = "",
        image=None,
        image_hover=None,
        color=None,
        action: EventType = None,
        name_action: str = "",
    ):
        super().__init__(x=x, y=y, width=width, height=height, image=image)
        self.font = pygame.font.SysFont("Arial", 24)
        self.text_surface = self.font.render(text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=(self.x, self.y))
        self.color = color
        self.current_color = color
        self.current_image = image
        self.image_hover = image_hover
        self.action = action
        self.name_action = name_action
        self.hover_time = 0
        self.scale = 1.0
        self.hover_threshold = 1.0  # seconds to trigger hold action

    def update(self, event_bus, cursor, delta_time):
        if not self.enabled:
            return

        is_hover = self._is_hovered(cursor)

        # ----------------------------
        # HOVER STATE
        # ----------------------------
        if is_hover:
            # emit hover (1 lần khi bắt đầu hover)
            if self.hover_time == 0:
                event_bus.emit(EventType.BUTTON_HOVER, {"target": self, "name": "button_hover"})

            self.hover_time += delta_time

            # visual feedback
            self.current_color = (200, 200, 200)
            self.current_image = self.image_hover if self.image_hover else self.image

            # ----------------------------
            # HOLD STATE
            # ----------------------------

            if self.hover_time >= self.hover_threshold:
                event_bus.emit(
                    EventType.BUTTON_HOLD,
                    {
                        "target": self,
                        "name": "button_hold",
                        "progress": self.hover_time / self.hover_threshold,
                    },
                )

                # ----------------------------
                # CLICK TRIGGER (hold complete)
                # ----------------------------
                event_bus.emit(EventType.BUTTON_CLICK, {"target": self, "name": "button_click"})

                # 🔥 ACTION EVENT (QUAN TRỌNG)
                if self.action:
                    event_bus.emit(self.action, {"name": self.name_action})

                # reset sau khi click
                self.hover_time = 0

        else:
            # reset khi rời khỏi button
            if self.hover_time > 0:
                event_bus.emit(EventType.BUTTON_UNHOVER, {"target": self, "name": "button_unhover"})

            self.hover_time = 0
            self.current_color = self.color
            self.current_image = self.image

    def _is_hovered(self, cursor):
        left = self.x - self.width / 2
        right = self.x + self.width / 2
        top = self.y - self.height / 2
        bottom = self.y + self.height / 2

        return left <= cursor.x <= right and top <= cursor.y <= bottom

    def get_render_data(self):
        if not self.enabled:
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
            "scale": self.scale,
            "button": True,
            "image": self.current_image or None,
        }
