# The word "polymorphism" means "many forms", 
# and in programming it refers to methods/functions/operators 
# with the same name that 
# can be executed on many objects or classes.

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def move(self):
        print("Drive!")

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in(car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()