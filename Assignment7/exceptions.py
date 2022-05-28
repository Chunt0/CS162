# Christopher Hunt
# CS162
# exceptions.py

class AnimalError(Exception):
    def __init__(self):
        super().__init__()
        print("***ANIMALERROR***")

class AnimalDies(AnimalError):
    def __init__(self):
        super().__init__()
        print("***ANIMALDIES***")

class AnimalExhaustion(AnimalError):
    def __init__(self):
        super().__init__()
        print("***ANIMALEXHAUSTION***")

