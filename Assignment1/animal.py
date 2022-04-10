# Christopher Hunt
# CS162


#### PART 2 ####

#### TAKE 1 - SIMPLE ANIMAL CLASS ####

class Animal:
    def __init__(self):
        self.name = None
        self.species = None 
        self.size = None
        self.external = None
        self.sound = None

    def setAttr(self):
        self.name = input("What's your animals name? ")
        self.species = input(f"What species is {self.name}? ")
        self.size = input(f"How big is {self.name}? ")
        self.external = input(f"What sort of external covering does {self.name} have? ")
        self.sound = input(f"What sound does {self.name} make? ")
    
    def printAttr(self):
        print(f"\nName: {self.name}\nSpecies: {self.species}\nSize: {self.size}\nExternal Covering: {self.external}\nSound: {self.sound}\n")

    def makeSound(self):
        print("\n")
        print(self.sound)

    def menu(self):
        select_on = True
        while(select_on == True):
            print("\n1. Set animal attributes\n2. Print attributes\n3. Make sound\n4. Quit\n")
            selection = input("## ")
            if(selection == "1"):
                self.setAttr()

            elif(selection == "2"):    
                self.printAttr()
                
            elif(selection == "3"):
                self.makeSound()
            
            elif(selection == "4"):
                print("\nBye Bye\n")
                select_on = False
            
            else:
                print("\nI don't know that command...\n")

