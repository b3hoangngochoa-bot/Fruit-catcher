from Models.base_entity import BaseEntity
import pygame


class Basket(BaseEntity):
    def __init__(self):
        super().__init__(width=100, height=50, color=(139, 69, 19), tag="BASKET")

    def update(self, input_data):
        if not self.active:
            return

        self.x = input_data["x"]
        self.y = input_data["y"]

    def draw(self, screen):
        if not self.active:
            return
        pygame.draw.rect(
            screen,
            self.color,
            (
                self.x - self.width // 2,
                self.y - self.height // 2,
                self.width,
                self.height,
            ),
        )
        # pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.height // 2)
        pass
