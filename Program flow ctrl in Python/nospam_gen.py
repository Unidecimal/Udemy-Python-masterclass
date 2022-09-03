menus = [
    ["egg", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "sausage", "bacon"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
]
# nospam with generator.
for meal in menus:
    items = ", ".join((item for item in meal if item != "spam"))
    print(items)
