class BasketModel:
    def __init__(self, position):
        self.position = position
        self.caught_fruits = 0

    def move(self, direction, delta_time):
        # Move the basket based on user input and delta_time
        pass

    def catch_fruit(self, fruit):
        # Check if the fruit is caught and update the score
        pass