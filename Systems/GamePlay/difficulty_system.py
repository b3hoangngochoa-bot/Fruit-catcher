class DifficultySystem:
    def __init__(self):
        self.level = 1

    def update(self, time_elapsed):
        """
        level tăng theo thời gian
        """
        self.level = int(time_elapsed // 10) + 1

    def get_spawn_speed_multiplier(self):
        return 1 + (self.level * 0.2)
