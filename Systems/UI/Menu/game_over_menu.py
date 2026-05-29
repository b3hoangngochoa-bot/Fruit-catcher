from Systems.UI.Menu.menu_base import MenuBase
from Systems.UI.Elements.button import Button
from Systems.UI.Elements.background import Background
from Systems.UI.Elements.label import Label
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
        image = load_ui_image("background","jpg", width=800, height=600)
        self.elements = [
            Label(x=350, y=100, size=50, text="Game Over", color=(255, 0, 0)),
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
