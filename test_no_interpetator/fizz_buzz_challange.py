import colour_print


def fizz_buzz(n: int) -> str:
    """
    Play fizz buzz - check what you shall say.
    :param n: The number to check.
    :return: a string with a number or,
        `Fizz` if it is divisible by 3.
        `Buzz` if it is divisible by 5.
        `Fizz Buzz` if it is divisible by both 3 and 5.
    """
    next_number = n
    if next_number % 3 == 0 and next_number % 5 == 0:
        return "fizz buzz"
    elif next_number % 3 == 0:
        return "fizz"
    elif next_number % 5 == 0:
        return "buzz"
    else:
        return str(next_number)


def check_player_answer(answer: str, number: int) -> bool:
    """
    Checking the answer in the guessing game `fizz buzz` if it is the
    right one.
    :param answer: The answer to be checked.
    :param number: The number being counted.
    :return: If in answer right: True, if wrong False.
    """
    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz" == answer.casefold()
    elif number % 3 == 0:
        return "fizz" == answer.casefold()
    elif number % 5 == 0:
        return "buzz" == answer.casefold()
    else:
        return str(number) == answer.casefold()


HUMAN = colour_print.colour_print("Human", colour_print.GREEN)
COMPUTER = colour_print.colour_print("Computer", colour_print.RED)
GOAL = 100
RULES = """ \n{0}: We count from 1 to 100, I start. 
If the number we count is divisible with 3 we say 'fizz' instead of the number,
if the number is divisible by 5 we say 'buss' and if it divisible 
with both 3 and 5 we say 'fizz buss' 

the game ends if you count wrong, I win. If you manage to reach {1},
 without telling wrong, you win. """.format(COMPUTER, GOAL)

player_input = ""
computer_count = ""
counter = 0
print("{0}: Lets play the game 'Fizz Buzz' the rules are simple: {1}".format(COMPUTER, RULES))
while True:
    counter += 1  # Advance counter for computer turn.
    computer_answer = fizz_buzz(counter)
    player_input = input("{0}: I count {1}, \n{2} your turn: "
                         .format(COMPUTER, colour_print.colour_print(
                            computer_answer, colour_print.RED), HUMAN))
    counter += 1  # Advance counter for Human turn.
    # test if players answer is wrong and if the goal is reached.
    right_answer = fizz_buzz(counter)
    if not right_answer == player_input:
        print("{0}: {1} you lose!".format(COMPUTER, HUMAN))
        break
    elif counter >= GOAL:
        print("{0}: {1} you have beaten me, I feel sad. ".format(COMPUTER, HUMAN))
        break

# for count in range(1, 50):
#       print("You counted: {0}, I counted: {1} ".format(count, fizz_buzz(count)))
#       print(check_player_answer(fizz_buzz(count), count))

