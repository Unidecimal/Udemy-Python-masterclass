list_of_choises = ["Exit", "Lern Python", "Lern Java", "Go unicycling", "Have"
                    " dinner", "Go to bed", "Re print choises" ]
printed = False
want_to_exit = False
max_choice = len(list_of_choises) - 1
user_choice = None

while want_to_exit != True:
    if printed is False:
        for choice in list_of_choises:
            print("{}:\t {}".format(list_of_choises.index(choice), choice))
        printed = True

    user_choice = int(input("Choose between 0 to {}, iput choice here: ".format(
        max_choice)))

    if user_choice == 0:
        print("You exit the program.")
        want_to_exit = True
    elif user_choice == max_choice:
        printed = False
    elif user_choice in range(1,max_choice):
        print("Your choice is: {}".format(list_of_choises[user_choice]))
    else:
        print("Your choice was: {}".format(user_choice))
        print("Yor choice must be one ofe the below list!")
        printed = False