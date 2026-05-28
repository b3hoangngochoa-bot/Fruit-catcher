from Models.base_entity import BaseEntity
from Models.fruit_type import FruitType
import pygame


class Fruit(BaseEntity):
    def __init__(
        self, x, y, width=40, height=40, vx=0, vy=0, image=None, fruit_type=None
    ):
        super().__init__(
            x=x, y=y, width=width, height=height, vx=vx, vy=vy, image=image, tag="FRUIT"
        )
        self.fruit_type = fruit_type
        self.score_value = (
            self._get_score()
        )  # Default score value, can be adjusted based on fruit type
        self.radius = width // 2  # Assuming fruit is circular for collision detection

        # debug color theo loại fruit
        self.color = self._get_color()

    def _get_score(self):
        if self.fruit_type == FruitType.APPLE:
            return 1
        elif self.fruit_type == FruitType.ORANGE:
            return 2
        elif self.fruit_type == FruitType.WATERMELON:
            return 3
        elif self.fruit_type == FruitType.BANANA:
            return 4

    def _get_color(self):
        if self.fruit_type == FruitType.APPLE:
            return (255, 0, 0)
        elif self.fruit_type == FruitType.ORANGE:
            return (255, 165, 0)
        elif self.fruit_type == FruitType.WATERMELON:
            return (0, 255, 0)
        elif self.fruit_type == FruitType.BANANA:
            return (255, 255, 0)

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
