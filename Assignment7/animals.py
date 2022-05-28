# Christopher Hunt
# CS162
# animals.py

################################################################################

class Animal():
    """Generic Animal class"""
    def __init__(self):
        """__init__"""
        self.HP = 100

    def eat(self):
        """Animals gotta eat. Restores one energy point."""
        print("Ate. Restored one energy point.")
        return 1

    def rest(self):
        """Animals gotta sleep. Restores one energy point."""
        print("Rested. Restored one energy point.")
        return 1

    def sound(self):
        """
        Animals make sounds. 
        This is essentially here to demonstrate polymorphism.
        """
        print("~~Animal sounds~~")

    def __string__(self):
        """Prints stats."""
        print(f"HP: {self.HP}")

################################################################################

class Bear(Animal):
    """Child class of Animal"""
    def __init__(self):
        """__init__"""
        super().__init__()
        self.speed = 1
        self.power = 3
        self.defense = 2
        self.energy = 3
        self.max_age = 16

    def run(self, p1loc, p2loc):
        """Moves Bear closer to opponent."""
        run = 0
        if p1loc < p2loc:
            run = self.speed
        if p1loc > p2loc:
            run = -self.speed

        return run

    def attack(self):
        """Causes damage to opponent."""
        return self.power

    def evade(self, p1loc, p2loc):
        """Moves Bear farther from opponent."""
        evade = 0
        if p1loc < p2loc:
            evade = -self.speed
        if p1loc > p2loc:
            evade = self.speed

        return evade

    def sound(self):
        """Bear makes a sound. Demonstrates polymorphism."""
        print("~Roaar~")

    def __string__(self):
        """Prints Bear's stats."""
        print(f"HP: {self.HP}\nSpeed: {self.speed}\nPower: {self.power}\nDefense: {self.defense}\nEnergy: {self.energy}\nMax Age: {self.max_age}")

################################################################################

class Eagle(Animal):
    """Child class of Animal"""
    def __init__(self):
        """__init__"""
        super().__init__()
        self.speed = 3
        self.power = 2
        self.defense = 1
        self.energy = 4
        self.max_age = 20

    def fly(self, p1loc, p2loc):
        """Moves Eagle closer to opponent."""
        fly = 0
        if p1loc < p2loc:
            fly = self.speed
        if p1loc > p2loc:
            fly = -self.speed

        return fly

    def attack(self):
        """Causes damage to opponent."""
        return self.power

    def evade(self, p1loc, p2loc):
        """Moves Eagle farther from opponent."""
        evade = 0
        if p1loc < p2loc:
            evade = -self.speed
        if p1loc > p2loc:
            evade = self.speed

        return evade

    def sound(self):
        """Eagle makes sound. Demonstrates polymorphism."""
        print("~Screee~")

    def __string__(self):
        """Prints Eagle's stats."""
        print(f"HP: {self.HP}\nSpeed: {self.speed}\nPower: {self.power}\nDefense: {self.defense}\nEnergy: {self.energy}\nMax Age: {self.max_age}")

################################################################################

class Salmon(Animal):
    """Child Class of Animal"""
    def __init__(self):
        """__init__"""
        super().__init__()
        self.speed = 2
        self.power = 1
        self.defense = 3
        self.energy = 6
        self.max_age = 24

    def swim(self, p1loc, p2loc):
        """Moves Salmon closer to opponent."""
        swim = 0
        if p1loc < p2loc:
            swim = self.speed
        if p1loc > p2loc:
            swim = -self.speed
        
        return swim

    def attack(self):
        """Causes damage to opponent."""
        return self.power

    def evade(self, p1loc, p2loc):
        """Moves Salmon farther from opponent."""
        evade = 0
        if p1loc < p2loc:
            evade = -self.speed
        if p1loc > p2loc:
            evade = self.speed
        return evade

    def sound(self):
        """Salmon makes sound? Demonstrates polymorphism."""
        print("~Glubglub~")
    
    def __string__(self):
        """Prints Salmon's stats."""
        print(f"HP: {self.HP}\nSpeed: {self.speed}\nPower: {self.power}\nDefense: {self.defense}\nEnergy: {self.energy}\nMax Age: {self.max_age}")
