import copy

animals = {"lion": ["scary", "big", "cat"],
           "elephant": ["big", "gray", "wise"],
           "teddy": ["cuddly", "stuffed", "googly eys"],
           }

print("-" * 10)

# Preform a shallow copy
# things = animals.copy()

# preform a deep copy
things = copy.deepcopy(animals)

print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])

print("-" * 10)
things["teddy"].append("toy")
print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])