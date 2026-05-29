from abc import ABC, abstractmethod
from Systems.Render.render_layer import RenderLayer


class UIElement(ABC):
    def __init__(self, x=0, y=0, width=0, height=0, image=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.enabled = True
        self.color = (255, 255, 255)  # Default color for debugging
        self.render_layer = RenderLayer.UI

    @abstractmethod
    def update(self, event_bus, cursor, delta_time):
        """
        Process interaction (hover, click, etc.)
        Return Event or None
        """
        pass

    @abstractmethod
    def get_render_data(self):
        """
        Get render data for the element
        """
        pass
