from Models.base_entity import BaseEntity
import pygame


class Cursor(BaseEntity):
    def __init__(self):
        super().__init__(width=10, height=10, color=(255, 255, 255), tag="CURSOR")

    def update(self, input_data):
        if not self.active:
            return

        self.x = input_data.get("x", 0)
        self.y = input_data.get("y", 0)

    def draw(self, screen):
        if not self.active:
            return
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.width)
        pass
