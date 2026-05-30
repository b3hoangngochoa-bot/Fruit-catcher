from Systems.UI.Menu.menu_base import MenuBase
from Systems.UI.Elements.button import Button
from Systems.UI.Elements.background import Background
from Core.event_type import EventType
from Utils import load_asset, constants

load_ui_image = load_asset.load_ui_image


class PauseMenu(MenuBase):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        """
        Create:
        - Resume button
        - Restart button
        - Back to menu button
        """
        background_image = load_ui_image(
            "background_pause_menu", "png", width=1280, height=720
        )
        resume_button_image = load_ui_image(
            "button_resume_normal", "png", width=200, height=100
        )
        resume_button_image_hover = load_ui_image(
            "button_resume_hover", "png", width=200, height=100
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
                y=constants.SCREEN_HEIGHT // 2,
                text="Resume",
                action=EventType.GAME_RESUME,
                color=(0, 255, 0),
                image=resume_button_image,
                image_hover=resume_button_image_hover,
                name_action="resume_game",
            ),
            Button(
                x=constants.SCREEN_WIDTH // 2,
                y=constants.SCREEN_HEIGHT // 2 + 120,
                text="Restart",
                action=EventType.GAME_RESTART,
                color=(255, 0, 0),
                image=restart_button_image,
                image_hover=restart_button_image_hover,
                name_action="restart_game",
            ),
            Button(
                x=constants.SCREEN_WIDTH // 2,
                y=constants.SCREEN_HEIGHT // 2 + 240,
                text="Back to Menu",
                action=EventType.GO_TO_MENU,
                color=(255, 255, 0),
                image=go_menu_button_image,
                image_hover=go_menu_button_image_hover,
                name_action="go_to_menu",
            ),
        ]
