animals = {"Turtle",
           "Horse",
           "Robbin",
           "Python",
           "Swallow",
           "Hedgehog",
           "Wren",
           "Aardvark",
           "Cat",
           }

birds = {'Robbin', 'Swallow', 'Wren'}

print(f'birds is a subset of animals: {birds.issubset(animals)}')
print(f"animals is a superset of birds: {animals.issuperset(birds)}")
print("the other way around")
print(f'birds is a superset of animals: {birds.issuperset(animals)}')
print("animals is a subset of birds: {}".format(animals.issubset(birds)))
print(birds <= animals)
print(birds < animals)

print('<>' * 80)
garden_birds = {'Swallow', 'Wren', 'Robbin'}
print(garden_birds == birds)
print(garden_birds <= birds)
print(garden_birds < birds) # check if garden_birds is a proper subset,
# Proper subsets ar always smaller than the proper superset.

print('*' * 80)
more_birds = {"Wren", "Budgie", "Swallow"}
print(garden_birds >= more_birds)