
# class Animal:
#     def __init__(self, nm):
#         self.name = nm
#         self.legs = 4 

#     def get_num_legs(self):
#         return self.legs
# # !!! the super class doesn't know anything about its subclasses !!!

# class Bird(Animal): # bird is a subclass of animal
#     def __init__(self, nm):
#         self.name = nm
#         self.legs = 2

# class Spider(Animal):
#     def __init__(self, nm):
#         self.name = nm
#         self.legs = 8 
#         # bird and spider inherit get_num_legs() and their self.legs override the superclass's self.legs

# '''
# Bird and Spider inherit the  get_num_legs() method from Animal. 
# By default, subclasses automatically inherit the methods and 
# attributes of their superclasses unless they override them.
# '''
# a1 = Animal('Annie')
# b1 = Bird('Polly')
# s1 = Spider('Charlotte')
# animals = [a1, b1, s1]

# for a in animals:
#     print(a.name, 'has', a.get_num_legs(), 'legs')

# =====================================================================================

class Animal:
  legs = 4 # class variable

  def __init__(self, nm):
    self.name = nm # instance variable

  def get_num_legs(self):
    return self.legs
  
  def greeting(self):
    return "cowers"
# !!! the super class doesn't know anything about its subclasses !!!

class Dog(Animal):

  def __init__(self, nm, br):
    super().__init__(nm)
    self.breed = br

  def greeting(self):
    return "wags"


class Labrador(Dog):
    def __init__(self, nm):
        super().__init__(nm, 'Labrador') # what's returned from super() is the class, not an instance of the class

    def greeting(self):
        print("in Labrlkadf.greeting()", self.name) # use print statements to debug and see what's happening
        return super().greeting() + " enthusiastically"

class Cow(Animal):
  pass

class Bird(Animal):
  legs = 2

class Spider(Animal): 
  legs = 8

a = Labrador("Midnight")
d1 = Dog('Fido',  'Dachsund')
c1 = Cow('Bessie')
b1 = Bird('Polly')
s1 = Spider('Charlotte')

# animals = [d1, c1, b1, s1]
# for a in animals:
#   print (a.name, 'has', a.get_num_legs(), 'legs and', a.greeting())

print(a.greeting())