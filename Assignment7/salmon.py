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
        self.max_age = 12

    def run(self):
        pass

    def attack(self):
        pass

    def evade(self):
        pass

    def sound(self):
        pass
