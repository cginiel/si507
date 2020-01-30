
class Pet:

    def __init__(self, nm, words=["woof", "arf", "yip"]):
        self.name = nm
        self.words = words

    def speak(self):
        my_words = ''
        for w in self.words:
            my_words += w + " "
        return "I can say " + my_words

    def teach(self, new_word):
        self.words.append(new_word)


if __name__ == "__main__": # useful because you can put only what you want to run here. it's like a dashboard.
    fido = Pet("fido")
    rufus = Pet("rufus")

    print(fido.speak())
    print(rufus.speak())

    fido.teach("rrrr")
    print(fido.speak())
    print(rufus.speak())