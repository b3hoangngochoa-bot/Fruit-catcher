from Models.base_entity import BaseEntity
from Models.fruit_type import FruitType


class Fruit(BaseEntity):
    def __init__(self, x, y, vx, vy, fruit_type: FruitType):
        super().__init__(x, y, 40, 40, vx, vy)
        self.fruit_type = fruit_type
        self.score_value = 1  # Default score value, can be adjusted based on fruit type

        # debug color theo loại fruit
        self.color = self._get_color()

    # def _get_score(self):
    #     if self.fruit_type == FruitType.APPLE:
    #         return 1
    #     elif self.fruit_type == FruitType.ORANGE:
    #         return 2
    #     elif self.fruit_type == FruitType.WATERMELON:
    #         return 3

    def _get_color(self):
        if self.fruit_type == FruitType.APPLE:
            return (255, 0, 0)
        elif self.fruit_type == FruitType.ORANGE:
            return (255, 165, 0)
        elif self.fruit_type == FruitType.WATERMELON:
            return (0, 255, 0)

    def draw(self, screen):
        pass
