# Christopher Hunt
# CS162
# animals.py

class Animal():
    def __init__(self):
        self.HP = 100
        
    def eat(self):
        print("Ate. Restored one energy point.")
        return 1

    def rest(self):
        print("Rested. Restored one energy point.")
        return 1

    def sound(self):
        print("~~Animal sounds~~")
    
    def __string__(self):
        print(f"HP: {self.HP}")

################################################################################

class Bear(Animal):
    def __init__(self):
        super().__init__()
        self.speed = 1
        self.power = 3
        self.defense = 2
        self.energy = 3
        self.max_age = 16

    def run(self, p1loc, p2loc):
        run = 0
        if p1loc < p2loc:
            run = self.speed
        if p1loc > p2loc:
            run = -self.speed

        return run

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
        print("~Roaar~")

    def __string__(self):
        print(f"HP: {self.HP}\nSpeed: {self.speed}\nPower: {self.power}\nDefense: {self.defense}\nEnergy: {self.energy}\nMax Age: {self.max_age}")

################################################################################

class Eagle(Animal):
    def __init__(self):
        super().__init__()
        self.speed = 3
        self.power = 2
        self.defense = 1
        self.energy = 4
        self.max_age = 20

    def fly(self, p1loc, p2loc):
        fly = 0
        if p1loc < p2loc:
            fly = self.speed
        if p1loc > p2loc:
            fly = -self.speed
            
        return fly

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
        print("~Screee~")
    
    def __string__(self):
        print(f"HP: {self.HP}\nSpeed: {self.speed}\nPower: {self.power}\nDefense: {self.defense}\nEnergy: {self.energy}\nMax Age: {self.max_age}")

################################################################################

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
    
    def __string__(self):
        print(f"HP: {self.HP}\nSpeed: {self.speed}\nPower: {self.power}\nDefense: {self.defense}\nEnergy: {self.energy}\nMax Age: {self.max_age}")
