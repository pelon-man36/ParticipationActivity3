from random import randint

class Die():
    def __init__(self, side=6):
        self.side = side

    def roll_die(self):
        list_of_ten = []
        for i in range(0, 10):
            output = randint(1, self.side)
            list_of_ten.append(output)
        print(list_of_ten)

my_die = Die()
my_die.roll_die()


