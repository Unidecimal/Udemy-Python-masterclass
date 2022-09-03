import random
highest = 1000
answer = random.randint(1, highest)
guess = 0
wrong = True
numbguess = 0


print("Please guess a number between 1 and {}: ".format(highest))
print('If you want to quit type "0"')

while wrong:
    guess = int(input())

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