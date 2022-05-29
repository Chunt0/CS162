# Christopher Hunt
# CS162
# pytests.py

from animals import Animal, Bear, Eagle, Salmon
from arena import Arena
from exceptions import AnimalDies, AnimalError, AnimalExhaustion
import random

def testEnergyDepletion():
    animal = Animal()

    energy = animal.energy
    animal.sound()
    assert energy > animal.energy # Make sure energy is going down when an action occurs

def testHealthDepletion():
    animal = Animal()

    health = animal.HP
    animal.damage(5)
    assert health > animal.HP # Make sure health went down after damage function

def testMoveFunction():
    for _ in range(100):
        animal1 = random.choice([Bear(random.randint(-10,10)), Eagle(random.randint(-10,10)), Salmon(random.randint(-10,10))])
        animal2 = random.choice([Bear(random.randint(-10,10)), Eagle(random.randint(-10,10)), Salmon(random.randint(-10,10))])
        
        move1 = animal1.move(animal2.pos)
        move2 = animal2.move(animal1.pos)
        if animal1.pos < animal2.pos:
            assert move1 > 0 and move2 < 0
        elif animal1.pos > animal2.pos:
            assert move1 < 0 and move2 > 0
        elif animal1.pos == animal2.pos:
            assert move1 == 0 and move2 == 0

