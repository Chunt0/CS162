# Christopher Hunt
# CS162
# animals.py

from exceptions import AnimalDies, AnimalExhaustion

################################################################################

class Animal():
    """Generic Animal class"""
    def __init__(self):
        """__init__"""
        self.name = "Animal"
        self.HP = 20
        self.energy = 3

    def eat(self):
        """Animals gotta eat. Restores one energy point."""
        self.energy += 1

    def damage(self, damage):
        self.HP -= damage
        self.checkHealth()

    def checkHealth(self):
        """Checks Animals health."""
        if self.HP > 0:
            return
        else:
            raise AnimalDies()

    def checkEnergy(self):
        """Checks Animals energy."""
        self.energy -= 1
        if self.energy >= 1:
            return
        else:
            raise AnimalExhaustion()

    def sound(self):
        """Animals make sounds. This is essentially here to demonstrate polymorphism."""
        
        self.energy -= 1
        self.checkEnergy()

        print("~~Animal sounds~~")

    def __str__(self):
        """Prints stats."""
        return f"HP: {self.HP}"

################################################################################

class Bear(Animal):
    """Child class of Animal"""
    def __init__(self, position):
        """__init__"""
        super().__init__()
        self.name = "Bear"
        self.speed = 1
        self.power = 3
        self.defense = 2
        self.energy = 9
        self.pos = position
        self.reach = 2

    def move(self, p2loc):
        """Moves Bear closer to opponent."""
        run = 0
        if self.pos < p2loc:
            run = self.speed
        if self.pos > p2loc:
            run = -self.speed
        
        self.checkEnergy()

        return run

    def attack(self):
        """Causes damage to opponent."""
        
        self.checkEnergy()

        return self.power

    def evade(self, p2loc):
        """Moves Bear farther from opponent."""
        evade = 0
        if self.pos < p2loc:
            evade = -self.speed
        if self.pos > p2loc:
            evade = self.speed

        self.checkEnergy()

        return evade

    def sound(self):
        """Bear makes a sound. Demonstrates polymorphism."""
        
        self.checkEnergy()

        print("~Roaar~")

    def __str__(self):
        """Prints Bear's stats."""
        return f"HP: {self.HP}\nName: {self.name}\nSpeed: {self.speed}\nPower: {self.power}\nDefense: {self.defense}\nEnergy: {self.energy}\nPosition: {self.pos}\n"

################################################################################

class Eagle(Animal):
    """Child class of Animal"""
    def __init__(self, position):
        """__init__"""
        super().__init__()
        self.name = "Eagle"
        self.speed = 3
        self.power = 2
        self.defense = 1
        self.energy = 12
        self.pos = position
        self.reach = 4

    def move(self, p2loc):
        """Moves Eagle closer to opponent."""
        fly = 0
        if self.pos < p2loc:
            fly = self.speed
        if self.pos > p2loc:
            fly = -self.speed
        
        self.checkEnergy()

        return fly

    def attack(self):
        """Causes damage to opponent."""
        
        self.checkEnergy()

        return self.power

    def evade(self, p2loc):
        """Moves Eagle farther from opponent."""
        evade = 0
        if self.pos < p2loc:
            evade = -self.speed
        if self.pos > p2loc:
            evade = self.speed
        
        self.checkEnergy()

        return evade

    def sound(self):
        """Eagle makes sound. Demonstrates polymorphism."""
        self.checkEnergy()

        print("~Screee~")

    def __str__(self):
        """Prints Eagle's stats."""
        return f"HP: {self.HP}\nName: {self.name}\nSpeed: {self.speed}\nPower: {self.power}\nDefense: {self.defense}\nEnergy: {self.energy}\nPosition: {self.pos}\n"

################################################################################

class Salmon(Animal):
    """Child Class of Animal"""
    def __init__(self, position):
        """__init__"""
        super().__init__()
        self.name = "Salmon"
        self.speed = 2
        self.power = 1
        self.defense = 3
        self.energy = 18
        self.pos = position
        self.reach = 4

    def move(self, p2loc):
        """Moves Salmon closer to opponent."""
        swim = 0
        if self.pos < p2loc:
            swim = self.speed
        if self.pos > p2loc:
            swim = -self.speed

        self.checkEnergy()

        return swim

    def attack(self):
        """Causes damage to opponent."""
        self.checkEnergy()

        return self.power

    def evade(self, p2loc):
        """Moves Salmon farther from opponent."""
        evade = 0
        if self.pos < p2loc:
            evade = -self.speed
        if self.pos > p2loc:
            evade = self.speed

        self.checkEnergy()

        return evade

    def sound(self):
        """Salmon makes sound? Demonstrates polymorphism."""

        self.checkEnergy()

        print("~Glubglub~")

    def __str__(self):
        """Prints Salmon's stats."""
        return f"HP: {self.HP}\nName: {self.name}\nSpeed: {self.speed}\nPower: {self.power}\nDefense: {self.defense}\nEnergy: {self.energy}\nPosition: {self.pos}\n"
