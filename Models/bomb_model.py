from Models.base_entity import BaseEntity
import pygame


class Bomb(BaseEntity):
    def __init__(self, x, y, vx, vy, damage=1):
        super().__init__(x, y, 40, 40, vx, vy, tag="BOMB")
        self.damage = damage  # Damage to the basket if hit
        self.color = (0, 0, 255)  # Bomb color for debugging

    def draw(self, screen):
        if not self.active:
            return
        pygame.draw.circle(
            screen, self.color, (int(self.x), int(self.y)), self.width // 2
        )
