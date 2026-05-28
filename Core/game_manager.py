from Core.event_type import EventType
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
        event_bus,
    ):
        self.input_system = input_system
        self.gameplay_system = gameplay_system
        self.collision_system = collision_system
        self.render_system = render_system
        self.ui_system = ui_system
        self.vision_system = vision_system
        self.audio_system = audio_system

        # Subscribe to game events
        self.event_bus = event_bus
        self.event_bus.subscribe(EventType.GAME_START, self._on_game_start)
        self.event_bus.subscribe(EventType.GAME_PAUSE, self._on_pause)
        self.event_bus.subscribe(EventType.GAME_RESUME, self._on_resume)
        self.event_bus.subscribe(EventType.GAME_OVER, self._on_game_over)

        self.state = Mode.PLAYING  # default state

    def game_loop(self):
        # Main game loop to update and render the game
        pass

    def update(self, delta_time):
        # 1. Lấy hand_data từ VisionSystem (đã được update() ở main loop)
        hand_data = self.vision_system.get_hand_data()

        # 2. Chuyển hand_data → input_data (pixel màn hình, đã làm mượt)
        input_data = self.input_system.update(hand_data)

        # 1. input
        # input_data = self.input_system.update()

        # 2. state-based update
        if self.state == Mode.MENU:
            self.ui_system.update(input_data, self.state)

        elif self.state == Mode.PLAYING:
            self.gameplay_system.update(input_data, delta_time)

        elif self.state == Mode.PAUSE:
            self.ui_system.update(input_data, self.state)

        elif self.state == Mode.GAME_OVER:
            self.ui_system.update(input_data, self.state)

    def draw(self):
        # Draw game objects and UI based on the current state
        self.render_system.draw()
    
    def _on_game_start(self, data):
        self.state = Mode.PLAYING

    def _on_pause(self, data):
        self.state = Mode.PAUSE

    def _on_resume(self, data):
        self.state = Mode.PLAYING

    def _on_game_over(self, data):
        self.state = Mode.GAME_OVER


