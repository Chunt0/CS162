class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.year = kwargs.get("year")
        self.capacity = kwargs.get("capacity")

    def __str__(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Capacity: {self.capacity}"

attributes = {"make": "ford", "model":"focus", "year":2010, "capacity":4}

car = Car(**attributes)

print(car)

# create a class, just define init metho using **kwargs
# read more about dunder methods
