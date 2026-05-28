import pygame
from Utils.constants import PATH_TO_IMAGES, PATH_TO_SOUNDS
from Models.fruit_type import FruitType


def _load_image(path, width=None, height=None):
    image = pygame.image.load(path).convert_alpha()
    if width and height:
        image = pygame.transform.scale(image, (width, height))
    return image

def load_basket_image(width, height):
    return _load_image(PATH_TO_IMAGES + "Basket/basket.png", width=width, height=height)

def load_fruit_image(fruit_type, width, height):
    if fruit_type == FruitType.APPLE:
        return _load_image(PATH_TO_IMAGES + "Fruits/apple.png", width=width, height=height)
    elif fruit_type == FruitType.ORANGE:
        return _load_image(PATH_TO_IMAGES + "Fruits/orange.png", width=width, height=height)
    elif fruit_type == FruitType.WATERMELON:
        return _load_image(PATH_TO_IMAGES + "Fruits/watermelon.png", width=width, height=height)
    elif fruit_type == FruitType.BANANA:
        return _load_image(PATH_TO_IMAGES + "Fruits/banana.png", width=width, height=height)

def load_bomb_image(width, height):
    return _load_image(PATH_TO_IMAGES + "Bomb/bomb.png", width=width, height=height)

def load_ui_image(name, width=None, height=None):
    return _load_image(PATH_TO_IMAGES + f"UI/{name}.png", width=width, height=height)