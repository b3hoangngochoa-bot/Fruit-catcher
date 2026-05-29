from Systems.UI.Menu.menu_base import MenuBase
from Systems.UI.Elements.button import Button
from Systems.UI.Elements.background import Background
from Core.event_type import EventType
from Utils.load_asset import load_ui_image


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
        image = load_ui_image("background", width=800, height=600)
        self.elements = [
            Background(image=image),
            Button(
                x=400,
                y=200,
                text="Start",
                action=EventType.GAME_START,
                color=(0, 255, 0),
            ),
            Button(
                x=400, y=300, text="Quit", action=EventType.QUIT_GAME, color=(255, 0, 0)
            ),
        ]
