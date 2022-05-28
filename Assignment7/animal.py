# Christopher Hunt
# CS162
# animal.py

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

