import utils
import re
import player

"""Player's chosen name, race, and profession"""
###Race###-------------------------------------------------------------------
DWARF = ('Dwarf', 0, 3)
ELF   = ('Elf', 2 , 1)
HUMAN = ('Human', 1, 2)

RACES =[DWARF, ELF, HUMAN]


def choose_race():
    n = len(RACES)
    print("Choose your character's race:")
    for idx,race in enumerate(RACES):
        print(f"{idx+1}. {race[0]}:\n"\
              f"   Dexterity: {race[1]}\n"\
              f"   Damage:    {race[2]}")
    idx = utils.input_num(f'Choose a race (1-{n}): ', n)-1
    return RACES[idx]

def race_check(race):
    print(f"Your race is {race._title}..." 
           "are you sure you would like to change it?")
    if utils.input_yes_no():
        return choose_race()
    else:
        return race

###Profession###-----------------------------------------------------------------
WARRIOR = ('Warrior', 15, 1)
ROGUE   = ('Rogue', 10, 5)
WARLOCK = ('Warlock', 12, 4)

PROFESSIONS = [WARRIOR, ROGUE, WARLOCK]


def choose_profession():
    print('Choose a class you wish to adventure as. Choose wisely.')
    print("Choose your character's class:")
    n = len(PROFESSIONS)
    for idx,prof in enumerate(PROFESSIONS):
        print(f"{idx+1}.  {prof[0]}:\n"\
              f"    HP:           {prof[1]}\n"\
              f"    Bonus Damage: {prof[2]}")

    idx = utils.input_num(f'Choose a profession (1-{n}): ', n)-1
    return PROFESSIONS[idx]


def prof_check(profession):
    print(f"Your profession is {profession._title}... "
           "are you sure you would like to change it?")
    if utils.input_yes_no():
        return choose_profession()
    else:
        return profession
###Name###----------------------------------------------------------------------------------   

def hero_name():
    while True:
        name = input('Please enter your name: ' )
        if name == '':
            print("That isn't a name.")
        elif len(name) > 18:
            print("Error! Only 15 characters allowed!")
        elif re.match("^[a-zA-Z]*$", name):
            return name
        else:
            print("Error! Only letters A-Z or a-z allowed!")

def name_check(name):
    """Makes sure name is preferred name"""
    print(f"Your name is {name}... "
           "Are you sure you would like to change it?")
    if utils.input_yes_no():
        return hero_name()
    else:
        return name
    
#--------------------------------------------------------------------
def character_creation():
    """Character creation"""
    print('Please identify yourself.')
    name = hero_name()
    race = choose_race()
    profession = choose_profession()
    me = player.Player(name, race, profession)
    return me

def menu():
    """Allows player to create a character and check thier status as well as add or remove gold"""
    me = None
    while True:
        options = ["Create Character", \
                   "Check Status", \
                   "Add Gold", \
                   "Remove gold", \
                   "Exit Menu"]
        menu_choice = utils.input_options("\nMenu options:", options)
        if menu_choice == 1:
            me = character_creation()
        elif menu_choice == 2:
            try: print(me.stats())
            except UnboundLocalError:
                print("You must create a character first.")
        elif menu_choice == 3:
            try:
                current = me.gold # so error shows before it asks for input
                amount  = int(input(f"How much gold do you want to add (you have {current} gold)? "))
                if amount >= 1000000:
                    print("Okay... now you're just abusing the system.")
                    amount = int(input("How much gold do you want to add? "))
                else:
                 me.add_gold(amount)
            except UnboundLocalError:
                    print("You must create a character first.")
        elif menu_choice == 4:
            try:
                current = me.gold # so error shows before it asks for input
                amount  = int(input(f"What amount would you like to remove (you have {current} gold)? "))
                me.remove_gold(amount)
            except UnboundLocalError:
                print("You must create a character first.")
        else:
            break


menu()