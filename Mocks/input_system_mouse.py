import pygame
import Utils.constants as constants


class MouseInputSystemMock:
    """
    Mock InputSystem dùng chuột thay vì Vision/tay.
    Output cùng format với InputSystem thật để dễ swap.
    """

    BASKET_RADIUS = 50

    def __init__(self):
        pass

    def update(self, hand_data=None) -> dict:
        """
        Lấy vị trí chuột và trả về input_data cùng format với InputSystem.
        Tham số hand_data bị bỏ qua (chỉ để tương thích interface).
        """
        mouse_x, mouse_y = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]

        return {
            "cursor": {
                "x": mouse_x,
                "y": mouse_y,
                "click": click,
            },
            "basket": {
                "x": mouse_x,
                "y": mouse_y,
                "radius": self.BASKET_RADIUS,
            },
        }
