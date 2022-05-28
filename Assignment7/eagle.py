
# Christopher Hunt
# CS162
# eagle.py
from animal import Animal

class Eagle(Animal):
    def __init__(self):
        super().__init__()
        self.speed = 3
        self.power = 2
        self.defense = 1
        self.energy = 4
        self.max_age = 10

    def fly(self, p1loc, p2loc):
        fly = 0
        if p1loc < p2loc:
            fly = self.speed
        if p1loc > p2loc:
            fly = -self.speed
            
        return fly

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
        print("~Screee~")
