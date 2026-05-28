from Core.game_state import Mode


class GameManager:
    def __init__(
        self,
        input_system,
        gameplay_system,
        collision_system,
        render_system,
        ui_system,
        vision_system,
        audio_system,
    ):
        self.input_system = input_system
        self.gameplay_system = gameplay_system
        self.collision_system = collision_system
        self.render_system = render_system
        self.ui_system = ui_system
        self.vision_system = vision_system
        self.audio_system = audio_system
        self.state = Mode.MENU

    def initialize(self):
        # Initialize all systems and game objects here
        pass

    def game_loop(self):
        # Main game loop to update and render the game
        pass

    def update(self, delta_time):
        # Lấy hand_data từ VisionSystem (đã được update() ở main loop)
        hand_data = self.vision_system.get_hand_data()

        # Chuyển hand_data → input_data (pixel màn hình, đã làm mượt)
        input_data = self.input_system.update(hand_data)

        # Cập nhật game logic
        self.gameplay_system.update(input_data, delta_time)

    def draw(self):
        # Draw game objects and UI based on the current state
        self.render_system.draw()
        pass

    def handle_events(self, events):
        # Handle user input and other events
        pass
