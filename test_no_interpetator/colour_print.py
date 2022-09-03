# Some ANSI escape sequences
# for colours:
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
# and effects:
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'
BLACK_BACKGROUND = '\u001b[40m'
RED_BACKGROUND = '\u001b[41m'
GREEN_BACKGROUND = '\u001b[42m'


def colour_print(text: str, *effects: str) -> str:
    """
    Print `text` using the ANSI sequence to change colour, etc.
    :param text: The text to print.
    :param effects: The effects we want. Zero or more of the constants defined at
     this module.
    :return: a string with color effects and reset.
    """
    effect_string = "".join(effects)
    return "{0}{1}{2}".format(effect_string, text, RESET)


print(colour_print("Hello!, Red", RED))
print(colour_print("Hello!, Red and bold", RED, BOLD))
print("This should be in the default terminal colour")
print(colour_print("Hello!, Blue", BLUE))
print(colour_print("Hello!, Blue reversed", BLUE, REVERSE))
print(colour_print("Hello!, Blue reversed, underline and bold", BLUE, BOLD, REVERSE, UNDERLINE))
print(colour_print("Hello!, Yellow", YELLOW))
print(colour_print("Hello!, Yellowand bold", YELLOW, BOLD))
print(colour_print("Hello!, Bold", BOLD))
print(colour_print("Hello!, Underline", UNDERLINE))
print(colour_print("Hello!, Reverse", REVERSE))
print(colour_print("Hello!, Black", BLACK))
