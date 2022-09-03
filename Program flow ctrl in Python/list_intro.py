computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]

for part in computer_parts:
    print(part)

print()
# using index on a list
print(computer_parts[2])

# using slice on a list
print(computer_parts[0:3])  # slicing a list producing a new list.
print(computer_parts[-1])

# different between list and strings are immutable which means that they
# can't be changed.
# Lists, are mutable, so you can change the content of a list.

# immutable types in Python.
# int, float, bool (subclass of int), str, tuple, frozenset, bytes