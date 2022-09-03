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
# challenge print without modifying list object.
for menu in menus:
    despamed_menue = ""
    for meal in menu:
        if meal != "spam":
            if despamed_menue == "":
                despamed_menue += "['{}'".format(meal)
            else:
                despamed_menue += ", '{}'".format(meal)
    print(despamed_menue + "]")

# challenge print out modified list.
for menu in menus:
    if "spam" in menu:
        top_index = len(menu) - 1
        for index_in_menu, meal in enumerate(reversed(menu)):
            if meal == "spam":
                del menu[top_index - index_in_menu]
for menu in menus:
    print(menu)
