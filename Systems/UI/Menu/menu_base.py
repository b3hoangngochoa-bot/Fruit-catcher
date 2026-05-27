from abc import ABC, abstractmethod


class MenuBase(ABC):
    def __init__(self):
        self.elements = []

    @abstractmethod
    def setup(self):
        """
        Create buttons / UI elements
        """
        pass

    def update(self, cursor):
        """
        Update all elements
        """
        for element in self.elements:
            event = element.update(cursor)
            if event:
                return event
        return None

    def draw(self, screen):
        """
        Draw all elements
        """
        for element in self.elements:
            element.draw(screen)
