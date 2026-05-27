import pygame


class MouseInputSystemMock:
    def __init__(self):
        pass

    def update(self):
        """
        Mock input từ mouse
        """
        mouse_x, mouse_y = pygame.mouse.get_pos()

        input_data = {"x": mouse_x, "y": mouse_y, "gesture": None}

        return input_data
