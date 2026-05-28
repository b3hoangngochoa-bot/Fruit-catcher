from Models.base_entity import BaseEntity
import pygame


class Bomb(BaseEntity):
    def __init__(self, x, y, width=50, height=50, vx=0, vy=0, image=None, damage=1):
        super().__init__(
            x=x, y=y, width=width, height=height, vx=vx, vy=vy, image=image, tag="BOMB"
        )
        self.damage = damage  # Damage to the basket if hit
        self.color = (0, 0, 255)  # Bomb color for debugging
        self.radius = width // 2  # Assuming bomb is circular for collision detection

    def get_render_data(self):
        if not self.active:
            return None

        return {
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height,
            "color": self.color,
            "radius": self.radius,
            "layer": self.render_layer,
            "shape": "circle",
            "image": self.image or None,
        }
