# import copy

# def many_params(p1=1, p2=2, p3=3, p4=4):
#     return p1 + p2 + p3 + p4
   
# # many_params can be called many different ways
# print(many_params())
# print(many_params(2, 4, 6, 8))
# print(many_params(p4=10))
# print(many_params(30, p3=40))
# print(many_params(p3=3, p1=6))

# # 1: 10
# # 2: 20
# # 3: 16
# # 4: 76
# # 5: 15

###############################################################
###############################################################

# class Pet:

#     def __init__(self, nm, words=["woof", "arf", "yip"]):
#         self.name = nm
#         self.words = copy.copy(words) 
#         # ^^^creates a copy so that other pets' words aren't touched. 
#         # but allows us to have a default mutable parameter

#     def speak(self):
#         my_words = ''
#         for w in self.words:
#             my_words += w + " "
#         return "I can say " + my_words

#     def teach(self, new_word):
#         self.words.append(new_word)

# fido = Pet("fido")
# rufus = Pet("rufus")

# fido.teach("bark")

# print(fido.speak())
# print(rufus.speak())

###############################################################
###############################################################

# import requests


# BASE_URL = "http://swapi.co/api/people" # only interested in people

# resp = requests.get(BASE_URL)
# results_object = resp.json() 
# people_list = results_object["results"]
# print(people_list[3]['name'], people_list[3]['eye_color'])
# exit()

###############################################################
###############################################################

'''
Refactor of starwars3.py to avoid hardcoding of species IDs
willy nilly throughout the code. Instead the speciesID-to-name 
mappings are managed by the function species_name.

'''

import requests

BASE_URL = "http://swapi.co/api/people" # only interested in people

SPECIES = {
    'https://swapi.co/api/species/1/': 'Human',
    'https://swapi.co/api/species/2/': 'Droid'
    }


def species_name(species_id):

    if species_id in SPECIES:
        return SPECIES[species_id]
    else:
        return 'Unknown'


class Character:


    def __init__(self, nm='', sp='', character_data=None):
        if (character_data is None):
            self.name = nm
            self.species = sp
        else:
            self.name = character_data['name']
            self.species = species_name(character_data["species"][0])


    def info(self):
        return self.name + " is a " + self.species


class Human(Character):


    def __init__(self, nm='', hc='Unkonwn', character_data=None):
        super().__init__(nm, 'Human', character_data=character_data)
        if (character_data is None):
            self.hair_color = hc
        else:
            self.hair_color = character_data['hair_color']


    def info(self):
        return super().info() + " who has " + self.hair_color + " hair"



#### Testing the Character class
luke = Human("Luke Skywalker (Test)", "sandy")
c3po = Character("C3PO (Test)", "Droid")

print(luke.info())
print(c3po.info())


#### Fetching Character data from swapi.co

resp = requests.get(BASE_URL)
results_object = resp.json() 
people_list = results_object["results"]
characters = []
for p in people_list:
    if species_name(p["species"][0]) == "Human":
        characters.append(Human(character_data=p))
    else:   
        characters.append(Character(character_data=p))

for c in characters:
    print(c.info())
