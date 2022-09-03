def print_shopping_cart(cart: list) -> str:
    """ Takes a list and format it to a pretty string even if empty """
    if len(cart) != 0:
        return_items = ""
        for items in cart:
            if return_items == "":
                return_items += f" {items}"
            else:
                return_items += f", {items}"
        return return_items
    else:
        return "The shopping cart is empty."


available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "mouse",
                   "4": "hdmi cable",
                   "5": "dvd drive",
                   "6": "ESDS disk",

                   }

computer_parts = []
current_choice = None

while current_choice != "0":
    if current_choice in available_parts and available_parts[current_choice] not in computer_parts:
        chosen_part = available_parts[current_choice]
        print(f"Adding {chosen_part}")
        computer_parts.append(chosen_part)
        print(f"Your copping cart contains below items:\n{print_shopping_cart(computer_parts)}")
    elif current_choice in available_parts and available_parts[current_choice] in computer_parts:
        chosen_part = available_parts[current_choice]
        print(f"Removing {chosen_part}")
        computer_parts.remove(chosen_part)
        print(f"Your copping cart contains below items:\n{print_shopping_cart(computer_parts)}")
    else:
        print("Please add items from the list below.")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: EXIT")
    current_choice = input(">")
