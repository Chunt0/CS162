# Christopher Hunt
# CS162
# arena.py

import random
from animals import Bear, Eagle, Salmon

class Arena():
    """Class object that allows for two animals to battle."""
    def __init__(self):
        self.player = random.choice([Bear(-5), Eagle(-5), Salmon(-5)])
        self.comp = random.choice([Bear(5), Eagle(5), Salmon(5)])

    def playerattack(self):
        pass

    def compAttack(self):
        pass

    def playerMove(self):
        pass

    def compMove(self):
        pass

    def playerEvade(self):
        pass

    def compEvade(self):
        pass

    def playerEat(self):
        pass

    def compEat(self):
        pass

    def playerSound(self):
        pass

    def compSound(self):
        pass

    def menu(self):
        """Menu function, used in driver to play game."""
        pass 
