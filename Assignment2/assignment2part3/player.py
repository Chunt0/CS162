import utils

#[!] This Player class is well designed and coherent to read.
#[!] The functionality of this class can easily be followed,
#[!] although I would suggest adding some comments at the beginning
#[!] to preface the role this class object will play in the over all
#[!] program.

class Player:
    def __init__(self, name, race, profession):
        self.name          = name
        self.race          = race[0]
        self.profession    = profession[0]
        self.gold          = 0
        self.cur_hp        = profession[1]
        self.max_hp        = profession[1]
        self.dex           = race[1]
        self.damage        = race[2] + profession[2] 

    def info(self):
        print(f'NAME :{self.name}\n'
              f'RACE :{self.race}\n'
              f'CLASS:{self.profession}\n')

    def stats(self):
        return f"\nPlayer Status:\n" \
               f"  NAME     : {self.name}\n" \
               f"  CLASS    : {self.profession}\n"\
               f"  GOLD     : {self.gold}\n" \
               f"  HP       : {self.cur_hp} / {self.max_hp}\n" \
               f"  DAMAGE   : {self.damage}\n" \
               f"  DEXTERITY: {self.dex}\n"

    def add_gold(self,amount):
        """Adds gold to the player's inventory"""
        if amount>=0:
            self.gold += amount
        else:
            print("Hilarious... you can't add negative gold.")
        
    def remove_gold(self,amount):
        """Removes gold from the players inventory"""
        if self.gold >= amount:
            self.gold -=amount
        else:
            print("We don't do credit here.")