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

    def run(self):
        pass

    def attack(self):
        pass

    def evade(self):
        pass

    def sound(self):
        pass
