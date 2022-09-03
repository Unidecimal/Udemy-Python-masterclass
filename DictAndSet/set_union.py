farm_animals = {"Cow", "Pig", "Sheep", "Hen", "Horse", "Goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse", "pig"}

all_animals_1 = farm_animals.union(wild_animals)
print(all_animals_1)

all_animals_2 = wild_animals.union(farm_animals)
print(all_animals_2)

all_animals_3 = wild_animals | farm_animals
print(all_animals_3)