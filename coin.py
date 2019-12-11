import random
class Coin:
    def __init__(self):
        self.__sideup = 'Heads'
    def flip(self):
        if random.randint(0,1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
    def get_sideup(self):
        return self.__sideup
coin = Coin()
