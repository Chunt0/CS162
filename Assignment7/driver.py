# Christopher Hunt
# CS162
# arena.py

import random
from animals import Bear, Eagle, Salmon

class Arena():
    """Class object that allows for two animals to battle."""
    def __init__(self, player):
        self.animals = [Bear(), Eagle(), Salmon()]
        self.player = random.choice(self.animals)
        self.comp = random.choice(self.animals)

