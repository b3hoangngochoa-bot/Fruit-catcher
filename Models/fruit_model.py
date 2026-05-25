class FruitModel:
    def __init__(self, fruit_type, position):
        self.fruit_type = fruit_type
        self.position = position
        self.caught = False

    def update(self, delta_time):
        # Update the fruit's position or state if necessary
        pass