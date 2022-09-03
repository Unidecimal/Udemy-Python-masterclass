parrot = "Norwegian Blue"

letter = input("Enter a character: ").lower()

if letter in parrot.lower():
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter.")
