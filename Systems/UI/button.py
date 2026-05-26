from UI.ui_element import UIElement

class Button(UIElement):
    def __init__(self, rect, action):
        super().__init__()
        self.rect = rect
        self.action = action
        self.hover_time = 0

    def update(self, cursor):
        """
        Detect hover / hold → return Event
        """
        return None

    def draw(self, screen):
        """
        Draw button UI
        """
        pass
