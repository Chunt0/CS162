# Christopher Hunt
# CS162
# arena.py

import random
from animals import Bear, Eagle, Salmon

class Arena():
    """Class object that allows for two animals to battle."""
    def __init__(self):
        self.left = -5 # As far left as Animals can go
        self.right = 5 # As far right as Animals can go
        self.player = random.choice([Bear(self.left), Eagle(self.left), Salmon(self.left)])
        self.comp = random.choice([Bear(self.right), Eagle(self.right), Salmon(self.right)])

    def playerattack(self):
        if abs((self.player.pos - self.comp.pos)) < self.player.reach:
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
