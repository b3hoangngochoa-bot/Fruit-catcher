from Systems.UI.Menu.menu_base import MenuBase
from Systems.UI.Elements.button import Button
from Systems.UI.Elements.background import Background
from Core.event_type import EventType
from Utils.load_asset import load_ui_image


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
        image = load_ui_image("background","jpg", width=800, height=600)
        self.elements = [
            Background(image=image),
            Button(
                x=400,
                y=200,
                text="Resume",
                action=EventType.GAME_RESUME,
                color=(0, 255, 0),
            ),
            Button(
                x=400,
                y=300,
                text="Restart",
                action=EventType.GAME_RESTART,
                color=(255, 0, 0),
            ),
            Button(
                x=400,
                y=400,
                text="Back to Menu",
                action=EventType.GO_TO_MENU,
                color=(255, 255, 0),
            ),
        ]
