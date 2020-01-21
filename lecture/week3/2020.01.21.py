# # import datetime

# # date_now = datetime.datetime.now()

# # print(date_now.year)
# # print(date_now.month)
# # print(date_now.day)

# # print(type(date_now))

# # class is a type of thing, object is a particular instance of that class!!!!!

# # BEGIN CLASS DEFINITION
# """
# class Dog:

#   def __init__(self, nm, br):
#     self.name = nm
#     self.breed = br
# """

# # END CLASS DEFINITION

# # every time we call "Dog" the program is going to
# # set up the function written above (which is how 
# # we "index" or call out the specific names below)

# d1 = Dog('Fido', 'German Shepherd')
# d2 = Dog('Rufus', 'Lhasa Apso')
# print (d1.name, 'is a', d1.breed)
# print (d2.name, 'is a', d2.breed)

# # "self" essentially equals d1 because self corresponds
# # to the object in question

# # in that sense, "self," in the case of d2
# # equals d2

# # "all class methods will have to have self as the first
# # parameter"


# class Dog:

#     large_dogs = ['German Shepherd', 'Golden Retriever',
#                   'Rottweiler', 'Collie',
#                   'Mastiff', 'Great Dane']
#     small_dogs = ['Lhasa Apso', 'Yorkshire Terrier',
#                   'Beagle', 'Dachshund', 'Shih Tzu']


#     def __init__(self, nm, br):
#         self.name = nm
#         self.breed = br


#     def speak(self):
#         if self.breed in Dog.large_dogs:
#             print('woof')
#         elif self.breed in Dog.small_dogs:
#             print('yip')
#         else:
#             print('rrrrr')


# d1 = Dog('Fido', 'German Shepherd')
# d2 = Dog('Rufus', 'Lhasa Apso')
# d3 = Dog('Fred', 'Mutt')

# d1.speak()
# d2.speak()
# d3.speak()

class Dog:

    large_dogs = ['German Shepherd', 'Golden Retriever',
                  'Rottweiler', 'Collie',
                  'Mastiff', 'Great Dane']
    small_dogs = ['Lhasa Apso', 'Yorkshire Terrier',
                  'Beagle', 'Dachshund', 'Shih Tzu']


    def __init__(self, nm, br, a):
        self.name = nm
        self.breed = br
        self.age = a

    def speak(self):
        if self.breed in Dog.large_dogs:
            print('woof')
        elif self.breed in Dog.small_dogs:
            print('yip')
        else:
            print('rrrrr')


def print_dog_years(d):
    '''prints a dog's name and age in dog years
    dog years = actual years * 7
    Parameters
    ----------
    dog : Dog
        The dog to print
    Returns
    -------
    none
    '''
    dog_years = d.age * 7
    print(f"{d.name} is a {d.breed} who is {dog_years} years old in dog years")
    pass #TODO: implement


kennel = [
    Dog('Fido', 'German Shepherd', 4),
    Dog('Rufus', 'Lhasa Apso', 7),
    Dog('Fred', 'Mutt', 11)
    ]

for dog in kennel:
    print_dog_years(dog)