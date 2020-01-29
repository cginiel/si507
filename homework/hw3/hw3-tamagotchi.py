from random import randrange
import random

## CONSTANTS ##

##Art by Hayley Jane Wakenshaw - https://www.asciiart.eu/animals/dogs
DOG_LEFT = """
   __
o-''|\_____/)
 \_/|_)     )
    \  __  /
    (_/ (_/ 
"""

DOG_RIGHT = """
        __
(\_____/|''-o
(     (_|\_/
 \  __   / 
  \_) \_) 
"""

##Art by Joan Stark - https://www.asciiart.eu/animals/cats
CAT_LEFT = """
 /\    /    
(' )  (
 (  \  )
 |(__)/
"""

CAT_RIGHT = """
\    /\\
 )  ( ')
(  /  )
 \(__)|
"""

class Pet:
    '''A Tamagotchi pet!
    Attributes
    ----------
    name : string
        The pet's name
    '''
    max_boredom = 6
    max_hunger = 10 # not attached to an instance bc it's a class attribute
    leaves_hungry = 16
    leaves_bored = 12

    ascii_art_left = ""
    ascii_art_right = ""

    # TODO: Add attribute "sound"
    def __init__(self, name, sound): # self refers to the instance of self. this indicates which instance you are working with. also, this is a constructor
        self.name = name # assigns the name the user gives to the instance
        self.sound = sound
        self.hunger = randrange(self.max_hunger)
        self.boredom = randrange(self.max_boredom)

    def mood(self):
        '''Get the mood of a pet. A pet can be happy, hungry or bored,
        depending on wether it was fed or has played enough.

        Parameters
        ----------
        none

        Returns
        -------
        str
            The mood of the pet
        '''

        if self.hunger <= self.max_hunger and self.boredom <= self.max_boredom:
            return "happy"
        elif self.hunger > self.max_hunger:
            return "hungry"
        else:
            return "bored"

    def status(self):
        '''Get the status of a pet to know its name, how it feels and what it wants.

        Parameters
        ----------
        none

        Returns
        -------
        str
            The name, mood and wants of the pet.
        '''

        state = "I'm " + self.name + '. '
        state += 'I feel ' + self.mood() + '. ' # here you recall mood method on this specific instance of "self."
        if self.mood() == 'hungry':
            state += 'Please feed me.'
        if self.mood() == 'bored':
            state += 'You can play with me.'
        return state

    def do_command(self, resp):
        '''Calls the appropriate methods of a pet based on command "resp" given by player.

        Parameters
        ----------
        resp : string
            The command to be issued to the pet.

        Returns
        -------
        none
        '''

        if resp == "speak":
            print(self.speak())
        elif resp == "play":
            self.play()
        elif resp == "feed":
            self.feed()
        elif resp == "wait":
            print("Nothing to do...")
        else:
            print("Please provide a valid command.")

    def has_left(self):
        '''Returns True if a pet has left the game due to hunger or boredom, otherwise False.

        Parameters
        ----------
        none

        Returns
        -------
        bool
            If a pet has left
        '''
        return self.hunger > self.leaves_hungry or self.boredom > self.leaves_bored

    def clock_tick(self):
        #TODO: implement function and add docstring
        self.hunger += 2
        self.boredom += 2

    def speak(self):
        #TODO: implement function and add docstring
        return "I say: " + self.sound

    def feed(self):
        #TODO: implement function and add docstring
        self.hunger -= 5
        if self.hunger <= 0:
            self.hunger = 0

    def play(self):
        #TODO: implement function and add docstring
        counter = 3
        
        while counter > 0:
            direction = random.randint(0, 1)
            guess = input("Does the pet look left or right?\n")
            answers = ["left", "right"]

            if guess in answers:
                #### right ####
                if direction == 0:
                    direction = "right"
                    if guess == direction:
                        print("Correct!")
                        self.boredom -= 5
                        if self.boredom <= 0:
                            self.boredom = 0
                        counter = 0
                    elif guess != direction:
                        print("I look to the right. Try again.")
                        print(self.ascii_art_right)

                #### left ####
                elif direction == 1:
                    direction = "left"
                    if guess == direction:
                        print("Correct!")
                        self.boredom -= 5
                        if self.boredom <= 0:
                            self.boredom = 0
                        counter = 0
                    elif guess != direction:
                        print("I look to the left. Try again.")
                        print(self.ascii_art_left)

                counter -= 1
            else:
                ("Invalid input. Try again.")


        print(f"boredom: {self.boredom}")
        print(f"hunger: {self.hunger}")


#######################################################################
#---------- Part 2: Inheritance - subclasses
#######################################################################

# TODO: Implement the Dog, Cat and Poodle subclasses and add docstrings

class Dog(Pet):
    ascii_art_right = DOG_RIGHT
    ascii_art_left = DOG_LEFT

    def speak(self):
        return super().speak() + ", arrrf!"
        

class Cat(Pet):
    ascii_art_right = CAT_RIGHT
    ascii_art_left = CAT_LEFT


    def __init__(self, name, sound, meow_count):
        super().__init__(name, sound)
        self.meow_count = meow_count

    def speak(self):
        return "I say: " + self.sound * meow_count


class Poodle(Dog):
    def dance(self):
        print("Dancing in circles like poodles do!")

    def do_command(self, resp):
        if resp == "dance":
            return self.dance()
        elif resp == "speak":
            self.dance()
        return super().do_command(resp)

def get_name():
    '''Asks the player which name a pet should have.

    Parameters
    ----------
    none

    Returns
    -------
    none
    '''
    return input("How do you want to name your pet?\n")


def get_sound():
    '''Asks the player what sound a pet should make

    Parameters
    ----------
    none

    Returns
    -------
    none
    '''
    return input("What does your pet say?\n")


def get_meow_count():
    '''Asks the player how often a cat should make a sound.

    Parameters
    ----------
    none

    Returns
    -------
    none
    '''
    while True:
        resp = input("How often does your Cat make a sound?\n")
        if resp.isnumeric():
            return int(resp)

p = None

while p == None:
    #### begin pet type selection ####
    resp_pet_type = input("What kind of pet would you like to adopt?\n")
    if resp_pet_type.isalpha():
        resp_pet_type = str(resp_pet_type)

#### DOG ####
        if resp_pet_type.lower() == "dog":

            #### begin pet name ####
            resp_name = get_name()
            while not resp_name.isalpha():
                print("Please use letters A - Z")
                resp_name = get_name()
            if resp_name.isalpha():
                resp_name = str(resp_name.title())

                #### begin pet sound ####
                resp_sound = get_sound()
                while not resp_sound.isalpha():
                    print("Please user letters A - Z")
                    resp_sound = get_sound()
                if resp_sound.isalpha():
                    resp_sound = str(resp_sound.title())

                #### begin pet instance call ####
                p = Dog(resp_name, resp_sound)
                # print(pet.status())
                # action = input("What should I do?\n")

#### CAT ####
        elif resp_pet_type.lower() == "cat":

            #### begin pet name ####
            resp_name = get_name()
            while not resp_name.isalpha():
                print("Please use letters A - Z")
                resp_name = get_name()
            if resp_name.isalpha():
                resp_name = str(resp_name.title())

                #### begin pet sound ####
                resp_sound = get_sound()
                while not resp_sound.isalpha():
                    print("Please user letters A - Z")
                    resp_sound = get_sound()
                if resp_sound.isalpha():
                    resp_sound = str(resp_sound)

                    #### get meow count ####
                    meow_count = get_meow_count()
                    # while not meow_count.isnumeric():
                    #     print("Please use numbers only.")
                    #     meow_count = get_meow_count()


                #### begin pet instance call ####
                p = Cat(resp_name, resp_sound, meow_count)

#### POoDLE ####
        elif resp_pet_type.lower() == "poodle":

            #### begin pet name ####
            resp_name = get_name()
            while not resp_name.isalpha():
                print("Please use letters A - Z")
                resp_name = get_name()
            if resp_name.isalpha():
                resp_name = str(resp_name.title())

                #### begin pet sound ####
                resp_sound = get_sound()
                while not resp_sound.isalpha():
                    print("Please user letters A - Z")
                    resp_sound = get_sound()
                if resp_sound.isalpha():
                    resp_sound = str(resp_sound.title())
                p = Poodle(resp_name, resp_sound)

        else:
            print(f"We only have dogs, cats, and poodles here!")



    # TODO: Instantiate either a cat, dog or poodle depending on the input
    # given by the player (case insenstive) and assign it to the variable p.
    # If the player does not provide valid input, print: 
    # "We only have Cats, Dogs and Poodles.". Continue the loop till
    # the player provides a vaild pet.

while not p.has_left():
    print()
    print(p.status())

    command = input("What should I do?\n")
    p.do_command(command)
    p.clock_tick()

print("Your pet has left.")