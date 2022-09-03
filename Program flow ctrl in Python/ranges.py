for i in range(-6, 21):
    print("i is now {}".format(i))

# if you not include a start value it defaults to 0.
for i in range(10):
    print("i is now {}".format(i))

# if you want to make steps of 2 just add a step value.
for i in range(0, 10, 2):
    print("i is now {}".format(i))

# you can use a negative step value, remember to have a greater start value than end value.
for i in range(10, 0, -2):
    print("i is now {}".format(i))

for i in range(0, 101, 7):
    print(i)
