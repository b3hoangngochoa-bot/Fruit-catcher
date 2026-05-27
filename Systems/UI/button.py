from UI.ui_element import UIElement

class Button(UIElement):
    def __init__(self, rect, text_surface, text_rect, action):
        super().__init__()
        self.rect = rect
        self.text_surface = text_surface
        self.text_rect = text_rect
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
