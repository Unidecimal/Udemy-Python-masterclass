activity = input("What would you like to do today?").casefold()

if "cinema".casefold() not in activity:
    print("But I want to go to the cinema")
else:
    print("That's funny i also want to go to the cinema!")
