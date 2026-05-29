from Core.event_type import EventType


class DifficultySystem:
    def __init__(self, event_bus):
        self.current_level = 1
        self._expected_level = 1
        self.event_bus = event_bus

    def update(self, time_elapsed):
        """
        level tăng theo thời gian
        """
        self._expected_level = int(time_elapsed // 10) + 1
        if self._is_level_up():
            self._handle_level_up()

    def get_spawn_speed_multiplier(self):
        return 1 + (self.current_level * 0.2)

    def _is_level_up(self):
        # Check if the level has increased based on time
        return self._expected_level > self.current_level

    def _handle_level_up(self):
        self.current_level = self._expected_level
        self.event_bus.emit(
            EventType.LEVEL_UP, {"level": self.current_level, "name": "level_up"}
        )
