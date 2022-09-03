from contents import recipes


def my_deepcopy(d: dict) -> dict:
    """
    Copy a dictionary, creating copies of the `list` or `dict` values.

    The function will crash with AttributeError if the values aren't
    list or dictionaries.

    :param d: The dictionary to copy.
    :return: A copy of `d`, with the values being copies of the original values.

    """
    copy_d = {}

    for item in d:
        copy_item = {}
        if type(d[item]) == dict or list:
            dict_list = d[item]
            for i in dict_list:
                copy_item[i] = dict_list[i]
            copy_d[item] = copy_item
        else:
            copy_d[item] = d[item]

    return copy_d


def teacher_deepcopy(d: dict) -> dict:
    """Teachers solution"""
    new_dict = {}
    for key, value in d.items():
        new_value = value.copy()
        new_dict[key] = new_value
    return new_dict


print("Padowans code")
recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
print("Yedi maser code")
recipes_copy_2 = teacher_deepcopy(recipes_copy)
recipes_copy_2["Butter chicken"]["ginger"] = 400
print(recipes_copy_2["Butter chicken"]["ginger"])
print(recipes_copy["Butter chicken"]["ginger"])

