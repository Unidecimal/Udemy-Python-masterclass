import shelve
import random

print(dir())
print(dir(__builtins__))
for m in dir(__builtins__):
    print(m)

print('*=' * 80)
print(dir())
print(dir(shelve))

print('*=' * 80)
for obj in dir(shelve.Shelf):
    if obj[0] != "_":
        print(obj)

# print help for imported module.
print('*=' * 80)
help(shelve)

# print help for funktion in module
print('*=' * 80)
help(random.randint)


