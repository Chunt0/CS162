# Christopher Hunt
# CS162
# kwargs.python

class Animal:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.species = kwargs.get("species")

        def __str__(self):
            return f"Name: {self.name}\nSpecies: {self.species}"

nella = {"name":"nella","species":"cat"}
meg = {"name":"meg","species":"human"}
chris = {"name":"chris","species":"human"}
caia = {"name":"caia","species":"dog"}

animals_list = (nella, meg, chris, caia)

animals = []

for animal in animals_list:
    object = Animal(**animal)
    animals.append(object)

print(animals[0])


