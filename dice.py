from random import randint

class Die():
    def __init__(self, side=6):
        self.side = side

    def roll_die(self):
        output = randint(1, self.side)
        print(output)

my_die = Die()
my_die.roll_die()


