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
        self.player = random.choice(\
                [Bear(self.left),\
                Eagle(self.left),\
                Salmon(self.left)])
        self.comp = random.choice(\
                [Bear(self.right),\
                Eagle(self.right),\
                Salmon(self.right)])

    def playerAttack(self):
        """Player attacks comp"""
        if abs((self.player.pos - self.comp.pos)) < self.player.reach:
            damage = (self.player.attack() * random.randint(1,5)) - self.comp.defense
            self.comp.damage(damage)
        else:
            self.player.checkEnergy()

    def compAttack(self):
        """Comp attacks player"""
        if abs((self.comp.pos - self.player.pos)) < self.comp.reach:
            damage = (self.comp.attack() * random.randint(1,5)) - self.player.defense
            self.player.damage(damage)
        else:
            self.comp.checkEnergy()

    def playerMove(self):
        """Player moves toward comp"""
        move = self.player.move(self.comp.pos)
        if (self.player.pos + move) < self.left:
            self.player.pos = self.left
        elif (self.player.pos + move) > self.right:
            self.player.pos = self.right
        else:
            self.player.pos += move

    def compMove(self):
        """Comp moves toward player"""
        move = self.comp.move(self.player.pos)
        if (self.comp.pos + move) < self.left:
            self.comp.pos = self.left
        elif (self.comp.pos + move) > self.right:
            self.comp.pos = self.right
        else:
            self.comp.pos += move

    def playerEvade(self):
        """Player moves away from comp"""
        move = self.player.evade(self.comp.pos)
        if (self.player.pos + move) < self.left:
            self.player.pos = self.left
        elif (self.player.pos + move) > self.right:
            self.player.pos = self.right
        else:
            self.player.pos += move

    def compEvade(self):
        """Comp moves away from player"""
        move = self.comp.evade(self.player.pos)
        if (self.comp.pos + move) < self.left:
            self.comp.pos = self.left
        elif (self.comp.pos + move) > self.right:
            self.comp.pos = self.right
        else:
            self.comp.pos += move

    def playerEat(self):
        """Player restores an energy point"""
        self.player.eat()

    def compEat(self):
        """Comp restores an energy point"""
        self.comp.eat()

    def playerSound(self):
        """Player makes a sound"""
        self.player.sound()

    def compSound(self):
        """Comp makes a sound"""
        self.comp.sound()

    def playerRound(self):
        """Moves through players round sequence"""
        print("\n\n\n\n########PLAYERROUND########\n1. Move\n2. Evade\n3. Attack\n4. Eat\n5. Sound\n")
        print(f"Player Health: {self.player.HP} | Player Energy: {self.player.energy} | Player Position: {self.player.pos}\nComp Health: {self.comp.HP} | Comp Energy: {self.comp.energy} | Comp Position: {self.comp.pos}")
        try:
            selection = int(input(":: "))
            if selection == 1:
                self.playerMove()
            elif selection == 2:
                self.playerEvade()
            elif selection == 3:
                self.playerAttack()
            elif selection == 4:
                self.playerEat()
            elif selection == 5:
                self.playerSound()
            else:
                print("You must not have entered an integer between 1 - 5\n")
                return
        except ValueError:
            print("You must enter an integer value.\n")

    def compRound(self):
        """Moves through comps round sequence"""
        selection = random.randint(1,4)
        if selection == 1 and self.comp.energy > 1:
            self.compMove()
        elif selection == 2 and self.comp.energy > 1:
            self.compEvade()
        elif selection == 3 and self.comp.energy > 1:
            self.compAttack()
        elif selection == 4 and self.comp.energy > 1:
            self.compSound()
        else:
            self.compEat()

    def menu(self):
        """Menu function, used in driver to play game."""
        print("\n\n\n~~~~Animal Battle Game~~~~")
        while True:
            self.playerRound()
            self.compRound()
