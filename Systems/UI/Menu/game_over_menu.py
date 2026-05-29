from Systems.UI.Menu.menu_base import MenuBase
from Systems.UI.Elements.button import Button
from Systems.UI.Elements.background import Background
from Core.event_type import EventType
from Utils import constants, load_asset

load_ui_image = load_asset.load_ui_image


class GameOverMenu(MenuBase):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        """
        Create:
        - Restart button
        - Back to menu button
        """
        background_image = load_ui_image(
            "background_game_over_menu", "png", width=1280, height=720
        )
        restart_button_image = load_ui_image(
            "button_restart_normal", "png", width=200, height=100
        )
        restart_button_image_hover = load_ui_image(
            "button_restart_hover", "png", width=200, height=100
        )
        go_menu_button_image = load_ui_image(
            "button_go_to_menu_normal", "png", width=200, height=100
        )
        go_menu_button_image_hover = load_ui_image(
            "button_go_to_menu_hover", "png", width=200, height=100
        )
        self.elements = [
            Background(image=background_image),
            Button(
                x=constants.SCREEN_WIDTH // 2,
                y=constants.SCREEN_HEIGHT // 2 + 130,
                text="Restart",
                action=EventType.GAME_RESTART,
                color=(255, 0, 0),
                image=restart_button_image,
                image_hover=restart_button_image_hover,
                name_action="restart_game",
            ),
            Button(
                x=constants.SCREEN_WIDTH // 2,
                y=constants.SCREEN_HEIGHT // 2 + 250,
                text="Back to Menu",
                action=EventType.GO_TO_MENU,
                color=(255, 255, 0),
                image=go_menu_button_image,
                image_hover=go_menu_button_image_hover,
                name_action="go_to_menu",
            ),
        ]
