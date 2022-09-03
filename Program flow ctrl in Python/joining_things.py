flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
]

# numbers = [
#     45,
#     40,
#     10,
#     90,
# ]

for flower in flowers:
    print(flower)

# Join iterate over a list. All the item must be of Type String.
# You can't join numbers forex ample

print(" | ".join(flowers))
# The teacher made it more "clear" see below
separator = ", "
output = separator.join(flowers)
print(output)

# print(", ".join(numbers))
