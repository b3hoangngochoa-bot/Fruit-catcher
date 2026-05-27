class GameplayState:
    def __init__(self):
        self.score = 0
        self.life = 3

        self.level = 1
        self.time_elapsed = 0  # seconds

    def add_score(self, value):
        self.score += value

    def lose_life(self, damage=1):
        self.life -= damage

    def is_game_over(self):
        return self.life <= 0
