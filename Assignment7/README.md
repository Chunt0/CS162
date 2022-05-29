# Assignment 7

Begin by reading design.txt. View UMLdiagram.pdf to see my class designs. 

How To Run:
- pull all .py files
- python3 /path/to/driver.py

This Program is an "Animal Battle" game. Essentially the player and the computer are
class objects that have various characteristics. These two objects exist on a number
line, player at -5 and comp at 5. You must get close enough to the opponent to attack.

The three most important are:
Health, Energy, and Position. 
If either player or comp's Health or Energy go to or below zero the exceptions made 
specifically for this assignment are raised and the program is exited. This game is 
turn based. Each round the player gets to decide to either: Move (move closer to 
opponent), Evade (move farther from opponent), Attack (cause a random amount of damage
to opponent), Eat (increase energy by 1), or Sound (animal makes it's specific sound). 

Some tips:
Keep an eye on your energy and health!

Eat a bunch of food at the beginning so your Energy level rises very high. This
makes it easier to test the other functions. 

Get as close to your opponent as possible. Each child Animal class has it's own 
range.
