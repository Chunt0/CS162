# Christopher Hunt
# CS162
# bear.py

from animal import Animal

class Bear(Animal):
    def __init__(self):
        super().__init__()
        self.speed = 1
        self.power = 3
        self.defense = 2
        self.energy = 3
        self.max_age = 8

    def run(self, p1loc, p2loc):
        run = 0
        if p1loc < p2loc:
            run = self.speed
        if p1loc > p2loc:
            run = -self.speed

        return run

    def attack(self):
        pass

    def evade(self, p1loc, p2loc):
        evade = 0
        if p1loc < p2loc:
            evade = -self.speed
        if p1loc > p2loc:
            evade = self.speed

        return evade

    def sound(self):
        print("~Roaar~")
