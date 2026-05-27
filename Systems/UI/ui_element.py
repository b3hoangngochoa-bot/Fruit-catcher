from abc import ABC, abstractmethod
from Systems.Render.render_layer import RenderLayer


class UIElement(ABC):
    def __init__(self):
        self.visible = True
        self.enabled = True
        self.render_layer = RenderLayer.UI

    @abstractmethod
    def update(self, cursor):
        """
        Process interaction (hover, click, etc.)
        Return Event or None
        """
        pass

    @abstractmethod
    def draw(self, screen):
        """
        Render element on screen
        """
        pass
