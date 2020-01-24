class Pet:
    def __init__(self, name, sound): # self refers to the instance of self. this indicates which instance you are working with. also, this is a constructor
        self.name = name # assigns the name the user gives to the instance
        self.sound = sound

class Dog(Pet): # even an empty class with a parent can take advantage of its parent's constructor
    pass
        
dog1 = Dog("Chase", "woof")
print(help(dog1))
print(dog1.sound)