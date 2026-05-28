class RenderSystem:
    def __init__(self, screen, gameplay_system):
        self.screen = screen
        self.gameplay_system = gameplay_system
    def draw(self, state, input_data):
        # draw everything based on state
        pass
    def draw(self):
        # clear screen
        self.screen.fill((0, 0, 0))  
        # 1. draw game objects
        self.gameplay_system.draw(self.screen)
    def draw_cursor(self, cursor):
        pass
    def draw_basket(self, basket):
        pass
    def draw_gameplay(self, gameplay_data):
        pass
    def draw_ui(self, ui_data):
        pass
