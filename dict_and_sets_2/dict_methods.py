d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "iv": "four",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

d2 = {
    7: "lucky seven",
    10: "ten",
    3: "this is the new tree",
    }

v = d.values()
print(v)

d[10] = "ten"
print(v)

print("four" in v)
print("eleven" in v)


print("Findig the key with douplicated lists and `if x in`")
keys = list(d.keys())
print(keys)
values = list(d.values())
print(values)
if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with the key {key}")

print("Findig the key with looping over key, value in d.items()")

for key, value in d.items():
    if value == "four":
        print(f"{d[key]} was found with the key {key}")


# Code for "The for `dict update method`" lecture.
# '-..-''-..-''-..-''-..-''-..-''-..-''-..-''-..-'
# # update takes the key value form the dict or tuple that we pass,
# # to it and update te dict keys with the new values.
# d.update(d2)
# for key, value in d.items():
#     print(key, value)
# print()
#
# d.update(enumerate(pantry_items))
# for key, value in d.items():
#     print(key, value)

# Code for "The remaining `dict` methods" lecture.
# '-..-''-..-''-..-''-..-''-..-''-..-''-..-''-..-'
# new_dict = dict.fromkeys(pantry_items, 0)
# print(new_dict)

# key = d.keys()
# print(key)
#
# # the below code works without te .keys() it is a rest from older python
# # versions. The code is more readable with .keys().
# for item in d.keys():
#     print(item)


