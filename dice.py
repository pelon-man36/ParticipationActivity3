from random import randint

class Die():
    """Simulates rolling a die
    
        Argument:
        side (default is 6)
    """
    def __init__(self, side=6):
        """Initialize die sides"""
        self.side = side

    def roll_die(self):
        """
        Rolls a die ten times.

        Returns: A list containing 10 random values.
        """
        list_of_ten = []
        for i in range(0, 10):
            output = randint(1, self.side)
            list_of_ten.append(output)
        print(list_of_ten)

default_six_sided = Die()
default_six_sided.roll_die()

ten_sided = Die(10)
ten_sided.roll_die()

twenty_sided = Die(20)
twenty_sided.roll_die()

