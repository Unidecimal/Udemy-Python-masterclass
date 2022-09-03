import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The String that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else: This will do exactly the same thing as the else block.
        # This is because the nothing else will be executed after return.
        print("The input: {} isn't a valid number!".format(temp))


highest = 1000
answer = random.randint(1, highest)
guess = 0
wrong = True
numbguess = 0


print("Please guess a number between 1 and {}: ".format(highest))
print('If you want to quit type "0"')

while wrong:
    guess = get_integer(": ")

    if guess == 0:
        print("You have quit the game, bye!")
        break
    elif guess < answer:
        print("Please guess higher.")
    elif guess > answer:
        print("Please guess lower.")
    else:
        if numbguess == 0:
            print("You got it the first time!")
        else:
            numbguess += 1
            print("You guessed right on {0} tries.".format(numbguess))
        wrong = False

    numbguess += 1
