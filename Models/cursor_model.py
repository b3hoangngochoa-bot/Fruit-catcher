from Models.base_entity import BaseEntity
import pygame


class Cursor(BaseEntity):
    def __init__(self):
        super().__init__(width=10, height=10, color=(255, 255, 255), tag="CURSOR")

    def update(self, input_data):
        if not self.active:
            return

        cursor = input_data.get("cursor", {})
        self.x = cursor.get("x") or 0
        self.y = cursor.get("y") or 0

    def draw(self, screen):
        if not self.active:
            return
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.width)
        pass
