class GamePlaySystem:
    def __init__(self, spawner):
        self.spawner = spawner
        self.fruits = []
        self.bombs = []

    def update(self, basket):
        # update objects
        # spawn new objects
        # return event if needed
        return None

    def reset(self):
        self.fruits.clear()
        self.bombs.clear()