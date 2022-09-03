from contents import pantry, recipes


def add_item_to_shop(data: dict, item: str, quantity: int) -> None:
    """ Add items and quantity to item_to_shop_dict"""
    # if item in item_to_shop_dict:
    #     data[item] += quantity
    # else:
    #     data[item] = quantity
    data[item] = data.setdefault(item, 0) + quantity

# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
# the abow row is a compensation

display_dict = {}
item_to_shop_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    # Display al menu of the recipes we know how to cook
    print("Please choose your recipe")
    print(".-''-..-''-..-''-..-''-..")
    for key, value in display_dict.items():
        print(f"{key} - {value}")
    print("0 - Exit program")
    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected: {selected_item}")
        print("checking ingredients ...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            required_in_pantry = pantry.get(food_item, 0)  # using defolt value '0' in the get method.
            if required_quantity <= required_in_pantry:
                print(f"\t{food_item} OK")

            else:
                required_to_buy = required_quantity - required_in_pantry
                print(f"\tYou need to buy: {required_to_buy} of {food_item}! ")
                add_item_to_shop(item_to_shop_dict, food_item, required_to_buy)
print("This is your list of item to buy:")
for item in sorted(item_to_shop_dict):
    quantity = item_to_shop_dict[item]
    print(f"{item} - {quantity}")
