# numbers = {*""} this creates a empty set but are not a pythonic way to code.
# this is used sometimes in tight loops and even in job intervenes.
# you can use {*{}} or {*[]} but this is even more obfuscated.
numbers = set()

print(numbers, type(numbers))
# numbers.add(1)
# print(numbers)
#
# while len(numbers) < 4:
#     next_value = int(input("Please enter your next value: "))
#     numbers.add(next_value)
# print(numbers)

data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# create a set from the list, to remove duplicates.
unique_data = sorted(set(data))
print(unique_data)

# Creating a list of unique colours, keeping the order they appeared.
unique_data = list(dict.fromkeys(data))
print(unique_data)
print()
print(dict.fromkeys(data))
