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
            damage = self.player.attack() * random.randint(1,5)
            self.comp.damage(damage)
        else:
            print("Player is out of range!")
            self.player.checkEnergy()

    def compAttack(self):
        if abs((self.comp.pos - self.player.pos)) < self.comp.reach:
            damage = self.comp.attack() * random.randint(1,5)
            self.player.damage(damage)
        else:
            print("Comp is out of range!")
            self.comp.checkEnergy()

    def playerMove(self):
        move = self.player.move(self.comp.pos)
        if (self.player.pos + move) < self.left:
            self.player.pos = self.left
        elif (self.player.pos + move) > self.right:
            self.player.pos = self.right
        else:
            self.player.pos += move

    def compMove(self):
        move = self.comp.move(self.player.pos)
        if (self.comp.pos + move) < self.left:
            self.comp.pos = self.left
        elif (self.comp.pos + move) > self.right:
            self.comp.pos = self.right
        else:
            self.comp.pos += move

    def playerEvade(self):
        move = self.player.evade(self.comp.pos)
        if (self.player.pos + move) < self.left:
            self.player.pos = self.left
        elif (self.player.pos + move) > self.right:
            self.player.pos = self.right
        else:
            self.player.pos += move

    def compEvade(self):
        move = self.comp.evade(self.player.pos)
        if (self.comp.pos + move) < self.left:
            self.comp.pos = self.left
        elif (self.comp.pos + move) > self.right:
            self.comp.pos = self.right
        else:
            self.comp.pos += move

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
