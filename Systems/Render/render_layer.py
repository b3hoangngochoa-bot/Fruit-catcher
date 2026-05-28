from enum import IntEnum


class RenderLayer(IntEnum):
    BACKGROUND = 0
    GAME_OBJECT = 1
    EFFECT = 2
    UI = 3
    OVERLAY = 4
