available_exits = ["north", "south", "east", "west"]

chosen_exit = ""

print("You are in a dark lit room with no visible exits, you feal stressed out and are starting to get "
      "panic!")
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction to run: ")
    if chosen_exit.casefold() == "quit":
        print("Exit game")
        break
else:
    print("aren't you glad you gor out of there?")


