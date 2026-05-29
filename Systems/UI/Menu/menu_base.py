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

    def update(self, input_data, event_bus, cursor, delta_time):
        for element in self.elements:
            element.update(input_data, event_bus, cursor, delta_time)

    def get_render_data(self):
        render_data = []

        for element in self.elements:
            rd = element.get_render_data()
            if rd:
                render_data.append(rd)
        return render_data
