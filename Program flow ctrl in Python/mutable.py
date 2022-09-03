# mutable objects in Python is
# list, dict, set, bytearray

shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))
shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
# the id remain the same after the added list with cookies. That means that
# Python don't destroy the object and kreate a new one as it does with
# strings that ar immutable.
print(another_list)

a = b = c = d = e = f = another_list

print(a)

print("Adding cream")

b.append("cream")
print(c)
print(d)
d.append("pizza kit")
print(e)
e.append("sausage")
print(f)
