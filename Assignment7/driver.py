# Christopher Hunt
# CS162
# arena.py

import random
from animals import Bear, Eagle, Salmon

class Arena():
    """Class object that allows for two animals to battle."""
    def __init__(self):
        self.animals = [Bear(), Eagle(), Salmon()]
        self.player = random.choice(self.animals)
        self.comp = random.choice(self.animals)
        self.map = [[0,0] for _ in range(0,10)]

    def menu(self):
        """Menu function, used in driver to play game."""

        

