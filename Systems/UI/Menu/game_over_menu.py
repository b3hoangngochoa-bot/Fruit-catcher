from Systems.UI.Menu.menu_base import MenuBase
from Systems.UI.button import Button
from Systems.UI.background import Background
from Core.event_type import EventType
from Utils.load_asset import load_ui_image


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
        image = load_ui_image("background", width=800, height=600)
        self.elements = [
            Background(image=image),
            Button(
                x=400,
                y=200,
                text="Restart",
                action=EventType.GAME_RESTART,
                color=(255, 0, 0),
            ),
            Button(
                x=400,
                y=300,
                text="Back to Menu",
                action=EventType.GO_TO_MENU,
                color=(255, 255, 0),
            ),
        ]
