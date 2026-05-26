class MouseInputSystemMock:
    def __init__(self):
        self.mouse_pos = (0, 0)
        self.mouse_buttons = (False, False, False)  # left, middle, right

    def update(self):
        # Simulate mouse movement and button presses
        self.mouse_pos = (100, 150)  # Example position
        self.mouse_buttons = (True, False, False)  # Simulate left button pressed

    def get_mouse_position(self):
        return self.mouse_pos

    def get_mouse_buttons(self):
        return self.mouse_buttons