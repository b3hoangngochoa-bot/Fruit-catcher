class Button:
    def __init__(self, rect, action):
        self.rect = rect
        self.action = action
        self.hover_time = 0

    def update(self, cursor):
        return None

    def draw(self, surface):
        pass
