# Christopher Hunt
# CS162
# salmon.py
from animal import Animal

class Salmon(Animal):
    def __init__(self):
        super().__init__()
        self.speed = 2
        self.power = 1
        self.defense = 3
        self.energy = 6
        self.max_age = 24

    def swim(self, p1loc, p2loc):
        swim = 0
        if p1loc < p2loc:
            swim = self.speed
        if p1loc > p2loc:
            swim = -self.speed
        
        return swim

    def attack(self):
        return self.power

    def evade(self, p1loc, p2loc):
        evade = 0
        if p1loc < p2loc:
            evade = -self.speed
        if p1loc > p2loc:
            evade = self.speed
        return evade

    def sound(self):
        print("~Glubglub~")
