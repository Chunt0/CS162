# Christopher Hunt
# CS162
# arena.py

import random
from animals import Bear, Eagle, Salmon

class Arena():
    """Class object that allows for two animals to battle."""
    def __init__(self, player):
        self.player = player
        self.comp = random.choice([Bear(), Eagle(), Salmon()])

