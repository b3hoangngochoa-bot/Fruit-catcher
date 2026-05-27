from Models.base_entity import BaseEntity

class Bomb(BaseEntity):
    def __init__(self, x, y, vx, vy, damage = 1):
        super().__init__(x, y, 40, 40, vx, vy)
        self.damage = damage  # Damage to the basket if hit
        self.color = (0, 0, 0)  # Bomb color for debugging

    def draw(self, screen):
        pass