class Dog: 
    def __init__(self ,name, breed, Owner):
        self.name  = name
        self.breed = breed
        self.Owner = Owner
    def bark(self):
        print("Woof! Woof!")

class Owner:
    def __init__(self, name, address):
        self.name = name
        self.address = address


Owner1 = Owner("jfifjeufh","3083904839048")
dog1 = Dog( "sigma", "bulldog", Owner1)
print(dog1.Owner.name)

dog2 = Dog("him", "poodle", Owner1)
dog2.bark()
print(f"{dog2.name} is a {dog2.breed}.")


