class InputSystem:
    def __init__(self, mapper, smoother):
        self.mapper = mapper
        self.smoother = smoother

    def update(self, hand_data):
        # Process user input, such as keyboard or mouse events
        cursor = {};
        basket = {};
        # Map hand positions to game coordinates

        input_data = {
            "cursor": cursor,
            "basket": basket
        }

        return input_data