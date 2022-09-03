animals_immut = {"lion": "scary",
                 "elephant": "big",
                 "teddy": "cuddly",
                 }

animals_mutab = {"lion": ["scary", "big", "cat"],
                 "elephant": ["big", "gray", "wise"],
                 "teddy": ["cuddly", "stuffed", "googly eys"],
                 }

things = animals_immut.copy()  # makes a copy of the dict
animals_immut["teddy"] = "toy"
print(things["teddy"])
print(animals_immut["teddy"])

print("-" * 10)
things = animals_mutab.copy()  # makes a copy of the dict this time shallow
print(things["teddy"])
print(animals_mutab["teddy"])

print("-" * 10)
things["teddy"].append("toy")
print(things["teddy"])
print(animals_mutab["teddy"])

