from Models.fruit_model import Fruit
from Models.bomb_model import Bomb
from Models.fruit_type import FruitType
from Models.basket_model import Basket
from random import choice, randint
from Utils import constants


class Spawner:
    def __init__(self):
        self._spawn_timer = 0
        self._spawn_delay = 1.0  # Spawn every 1 second (adjust as needed)
        self.fruit_types = [
            FruitType.APPLE,
            FruitType.ORANGE,
            FruitType.WATERMELON,
            FruitType.BANANA,
        ]
        self.basket = Basket()

    def update(self, object_manager, delta_time, difficulty_multiplier=0):

        self._spawn_timer += delta_time
        if self._spawn_timer < self._spawn_delay:
            return
        self._spawn_timer = 0

        self._random_spawn(object_manager, difficulty_multiplier)

    def spawn(self, object_manager, fruit_type=None, difficulty_multiplier=0):
        """
        Spawn a new fruit or bomb and add it to the object manager
        """
        if fruit_type is not None:
            # Spawn a fruit
            new_fruit = Fruit(
                x=randint(50, constants.SCREEN_WIDTH - 50),  # Random x position within screen bounds
                y=-10,  # Start above the screen
                vx=0,
                vy=30 * difficulty_multiplier,  # Random falling speed
                fruit_type=fruit_type,
            )
            object_manager.add_object(new_fruit)
            # print(f"Spawned a {new_fruit.tag} at x={new_fruit.x}, y={new_fruit.y}")
            return new_fruit
        else:
            # Spawn a bomb
            new_bomb = Bomb(
                x=randint(50, constants.SCREEN_WIDTH - 50),
                y=-10,
                vx=0,
                vy=30 * difficulty_multiplier,  # Bombs can fall faster than fruits
            )
            object_manager.add_object(new_bomb)
            # print(f"Spawned a {new_bomb.tag} at x={new_bomb.x}, y={new_bomb.y}")
            return new_bomb

    def _random_spawn(self, object_manager, difficulty_multiplier=0):

        # Randomly decide to spawn a fruit or a bomb
        random_value = randint(1, 100)
        if random_value <= 80:  # 80% chance to spawn a fruit
            # print(f"Spawning a fruit with chance = {random_value}")
            fruit_type = choice(self.fruit_types)
            return self.spawn(object_manager, fruit_type, difficulty_multiplier)
        else:  # 20% chance to spawn a bomb
            # print(f"Spawning a bomb with chance = {random_value}")
            return self.spawn(object_manager, None, difficulty_multiplier)
