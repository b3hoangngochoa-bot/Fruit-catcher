import pygame


class MouseInputSystemMock:
    def __init__(self):
        pass

    def update(self):
        """
        Mock input từ mouse
        """
        mouse_x, mouse_y = pygame.mouse.get_pos()

        input_data = {
            "x": mouse_x,
            "y": mouse_y,
            "is_click": pygame.mouse.get_pressed()[0],
            "gesture": None  # future: vision system
        }

        return input_data
