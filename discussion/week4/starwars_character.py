

class Character:


    def __init__(self, nm='', sp='', character_data=None):
        if (character_data is None):
            self.name = nm
            self.species = sp
        else:
            self.name = character_data['name']
            if (character_data["species"][0] 
                    == "https://swapi.co/api/species/1/"):
                self.species = "Human"
            elif (character_data["species"][0]
                    == "https://swapi.co/api/species/2/"):
                self.species = "Droid"
            else:
                self.species = "Unknown"
                

    def info(self):
        return self.name + " is a " + self.species


#### Testing the Character class

if __name__ == "__main__":
    luke = Character("Luke Skywalker (Test)", "Human") # instantiation of some characters
    c3po = Character("C3PO (Test)", "Droid")

    print(luke.info())
    print(c3po.info())
else:
    print("Running as an imported module", __name__)

print(__name__)