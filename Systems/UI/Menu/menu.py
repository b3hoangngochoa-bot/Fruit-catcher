from Systems.UI.Menu.menu_base import MenuBase
from Systems.UI.Elements.button import Button
from Systems.UI.Elements.background import Background
from Core.event_type import EventType
from Utils import load_asset, constants

load_ui_image = load_asset.load_ui_image


class Menu(MenuBase):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        """
        Create:
        - Start button
        - Quit button
        """
        background_image = load_ui_image(
            "background_menu", "png", width=1280, height=720
        )
        start_button_image = load_ui_image(
            "button_start_normal", "png", width=200, height=100
        )
        start_button_image_hover = load_ui_image(
            "button_start_hover", "png", width=200, height=100
        )
        quit_button_image = load_ui_image(
            "button_quit_normal", "png", width=200, height=100
        )
        quit_button_image_hover = load_ui_image(
            "button_quit_hover", "png", width=200, height=100
        )
        self.elements = [
            Background(image=background_image),
            Button(
                x=constants.SCREEN_WIDTH // 2,
                y=constants.SCREEN_HEIGHT // 2 - 50,
                text="Start",
                action=EventType.GAME_START,
                color=(0, 255, 0),
                image=start_button_image,
                image_hover=start_button_image_hover,
                name_action="game_start",
            ),
            Button(
                x=constants.SCREEN_WIDTH // 2,
                y=constants.SCREEN_HEIGHT // 2 + 100,
                text="Quit",
                action=EventType.QUIT_GAME,
                color=(255, 0, 0),
                image=quit_button_image,
                image_hover=quit_button_image_hover,
                name_action="quit_game",
            ),
        ]
