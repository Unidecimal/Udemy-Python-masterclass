available_parts = { "1": "computer",
                    "2": "monitor",
                    "3": "mouse",
                    "4": "hdmi cable",
                    "5": "dvd drive",
                    "6": "ESDS disk",

}

computer_parts = {}  # creating a empty dict.
current_choice = None
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            # it's already in so remove it.
            print(f"Removing: {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
        print(f"Your cart now contains: {computer_parts}")
    else:
        print("Please add items from the list below.")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: EXIT")
    current_choice = input(">")

