import pet

p1 = pet.pets[0]
p2 = pet.Pet("Polly", ["cracker", "scurvy dog"])

# print(p1.speak()) # you have to use a method for your object to *do* anything. in this case, speak()
# print(p2.speak())

pet.teach_random(p1, 2)
pet.teach_random(p2, 3)

# print(p1.speak())
# print(p2.speak())
