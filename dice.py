from random import randint

class Die(sides=6):
    def __init__(self, side):
        self.side = side

    def roll_die(self):
        randint(1, self.side)

