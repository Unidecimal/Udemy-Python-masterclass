low = 1
high = 1000

print("Think of a number between {} and {}.".format(low, high))
input("Pres ENTER to start.")

guesses = 1

while low != high:
    # print("\t[ Computer thinking ] - Guessing in the rage of {} to {}"
    # .format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. \nShould I guess higher or lower?"
                     " Press h or l, or c if my guess was correct?: "
                     .format(guess)).casefold()
    if high_low == "h":
        # Guess higher. The lower end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes one less than the guess.
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l or c.")

    guesses += 1
else:
    print("The number you thinking of must be {}, i guessed it after {} "
          "guesses!".format(low, guesses))
