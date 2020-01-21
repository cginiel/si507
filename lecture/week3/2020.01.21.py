# import datetime

# date_now = datetime.datetime.now()

# print(date_now.year)
# print(date_now.month)
# print(date_now.day)

# print(type(date_now))

# class is a type of thing, object is a particular instance of that class!!!!!

# BEGIN CLASS DEFINITION
"""
class Dog:

  def __init__(self, nm, br):
    self.name = nm
    self.breed = br
"""

# END CLASS DEFINITION

# every time we call "Dog" the program is going to
# set up the function written above (which is how 
# we "index" or call out the specific names below)

d1 = Dog('Fido', 'German Shepherd')
d2 = Dog('Rufus', 'Lhasa Apso')
print (d1.name, 'is a', d1.breed)
print (d2.name, 'is a', d2.breed)

# "self" essentially equals d1 because self corresponds
# to the object in question

# in that sense, "self," in the case of d2
# equals d2

# "all class methods will have to have self as the first
# parameter"


class Dog:

    large_dogs = ['German Shepherd', 'Golden Retriever',
                  'Rottweiler', 'Collie',
                  'Mastiff', 'Great Dane']
    small_dogs = ['Lhasa Apso', 'Yorkshire Terrier',
                  'Beagle', 'Dachshund', 'Shih Tzu']


    def __init__(self, nm, br):
        self.name = nm
        self.breed = br


    def speak(self):
        if self.breed in Dog.large_dogs:
            print('woof')
        elif self.breed in Dog.small_dogs:
            print('yip')
        else:
            print('rrrrr')


d1 = Dog('Fido', 'German Shepherd')
d2 = Dog('Rufus', 'Lhasa Apso')
d3 = Dog('Fred', 'Mutt')

d1.speak()
d2.speak()
d3.speak()