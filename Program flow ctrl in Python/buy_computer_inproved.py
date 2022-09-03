current_choice = "-"
computer_parts = []  # create an empty list
available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi-cable",
                   "modem",
                   "DVD-Drive"
                   ]

# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

while current_choice != '0':
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # it's already in, so remove it.
            answer = "-"
            while answer not in "YyNn":
                answer = input("Do you want to remove it Y/N?: ")
                if answer in "Yy":
                    computer_parts.remove(chosen_part)
                    print("Removing {}".format(chosen_part))
                    current_choice = "-"
                elif answer in "Nn":
                    computer_parts.append(chosen_part)
                    print("Adding {}".format(current_choice))
        else:
            computer_parts.append(chosen_part)
            print("Adding {}".format(current_choice))
    else:
        print("Please add options from the list below:")
        #  There are a more efficient way to write the code using the
        #  enumerate function.
        # for part in available_parts:
        #     print("{0}: {1}".format(available_parts.index(part) + 1, part))
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))
        print("0: exit program")

    print("Your list now contains: {}".format(computer_parts))
    current_choice = input()

print(computer_parts)
