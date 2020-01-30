import requests
import starwars_character

#### Fetching Character data from swapi.co
BASE_URL = "http://swapi.co/api/people" # only interested in people

resp = requests.get(BASE_URL)
results_object = resp.json() 
people_list = results_object["results"]
characters = []
for p in people_list:
    characters.append(starwars_character.Character(character_data=p)) # you have to give this file the module's name, then follow with the class

for c in characters:
    print(c.info())


##### __name__ evaluates to the name of the current module

#### you're always running the main file. that's why it's main.