import unittest
import pet

class TestPet(unittest.TestCase):

    def testConstructor(self):
        p1 = pet.Pet("fido")
        p2 = pet.Pet("rufus", ["bark", "woof"])
        self.assertEqual(p1.name, "fido")
        self.assertEqual(p2.name, "rufus")
        self.assertEqual(p2.words[0], "bark")

    def testTeach(self):
        p1 = pet.pets[0]
        p2 = pet.Pet("rufus")

        self.assertEqual(len(p1.words), 2)
        self.assertEqual(len(p2.words), 2)

        p1.teach("hello")

        self.assertEqual(len(p1.words), 3)
        self.assertEqual(len(p2.words), 2)

    def testSpeak(self):
        p1 = pet.pets[0]
        p2 = pet.Pet("Polly", ["cracker", "scurvy dog"])

        self.assertEqual(p1.speak(), "I can say hi bye")
        self.assertEqual(p2.speak(), "I can say cracker scurvy dog")




#### Run the tests
print("pet_test.py module name is", __name__)
unittest.main()