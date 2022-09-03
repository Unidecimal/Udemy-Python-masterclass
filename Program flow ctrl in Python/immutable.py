# immutable types in Python.
# int, float, bool (subclass of int), str, tuple, frozenset, bytes

# result = True
# another_result = result
# print(id(result))
# print(id(another_result))
# # if bool values can be change the id should not change if we're changing
# # the value.
#
# result = False
# print(id(result))

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result = result.replace("C", "P")
print(id(result))





