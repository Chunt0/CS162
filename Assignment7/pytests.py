# Christopher Hunt
# CS162
# pytests.py

from animals import Animal, Bear, Eagle, Salmon
import random

def testEnergyDepletion():
    """Runs 100 tests to make sure animal.energy is going down when sound() is called."""
    for _ in range(100):
        animal = random.choice([Bear(random.randint(-10,10)), Eagle(random.randint(-10,10)), Salmon(random.randint(-10,10))])
        energy = animal.energy
        random.choice([animal.sound(), animal.move(0), animal.evade(0), animal.attack()])
        assert energy > animal.energy # Make sure energy is going down when an action occurs

def testHealthDepletion():
    """Runs 100 tests to make sure animal.HP is decreasing when damage() is called"""
    for _ in range(100):
        animal = random.choice([Bear(random.randint(-10,10)), Eagle(random.randint(-10,10)), Salmon(random.randint(-10,10))])
        health = animal.HP
        animal.damage(5)
        assert health > animal.HP # Make sure health went down after damage function

def testMoveFunction():
    """
    Runs 100 tests to make sure move() works properly - animal.pos is adjusted
    in the correct direction: positive, negative, or zero if they are equal.
    """
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

