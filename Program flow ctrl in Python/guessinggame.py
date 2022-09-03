answer = 5
guess = 0
wrong = True
numbguess = 0

while wrong:
    print("Please guess a number between 1 and 10: ")
    guess = int(input())
    if guess < answer:
        print("Please guess higher.")
        numbguess += 1
    elif guess > answer:
        print("Please guess lower.")
        numbguess += 1
    else:
        if numbguess == 0:
            print("You got it the first time!")
        else:
            print("You guessed right on {0} tries.".format(numbguess))
        wrong = False
