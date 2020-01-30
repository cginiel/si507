import unittest
import pet_main

class TestPet(unittest.TestCase):

    def testConstructor(self):
        p1 = pet_main.Pet("fido")
        p2 = pet_main.Pet("rufus", ["bark", "woof"])
        self.assertEqual(p1.name, "fido")
        self.assertEqual(p2.name, "rufus")
        self.assertEqual(p2.words[0], "bark")

    def testTeach(self):
        p1 = pet_main.Pet("fido")
        p2 = pet_main.Pet("rufus")

        self.assertEqual(len(p1.words), 3)
        self.assertEqual(len(p2.words), 3)

        p1.teach("hello")

        self.assertEqual(len(p1.words), 4)
        self.assertEqual(len(p2.words), 3)



#### Run the tests
unittest.main()