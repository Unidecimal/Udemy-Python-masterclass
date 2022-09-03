panagram = """The quick brown
    fox jumps\tover 
    the lazy dog"""

# plit returns a list with words as elements.
words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
# print(numbers.split(","))
print("_-´'`-_," * 8)
values_list = numbers.split(",")
print(values_list)
number_string = " ".join(values_list)
print(number_string)
values_list = number_string.split(" ")
print(values_list)
# challenge my solution
for index, number in enumerate(values_list):
    values_list[index] = int(number)
print("_-´'`-_," * 8)
print("My solution:        {}".format(values_list))
print("_-´'`-_," * 8)
# teachers solution
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])
print("Teacher solution 1: {}".format(values_list))
print("_-´'`-_," * 8)

# create a new list
integer_values = []
for value in values_list:
    integer_values.append(int(value))
print("Teacher solution 2: {}".format(integer_values))
print("_-´'`-_," * 8)

