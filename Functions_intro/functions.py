def multiply():
    """
    Multiples one `float` and one `int`
    :return: returns a `float`
    """
    result = 10.5 * 4
    return result


def multiply_advance(number_1: float, number_2: float) -> float:
    """
    The function is intended to multiply two numbers. But it is possible
    to multiply two sequences, it is not intended thou. If you pass a
    sting as the first argument and a number as the second argument,
    you get the string repeated `number_2` times as the return value.

    :param number_1: The first of the numbers that shall be multiplied.
    :param number_2: The number to multiply `number_1` by.
    :return: The product of `number_1` and `number_2`
    """
    result = number_1 * number_2
    return result


def is_palindrome(string: str) -> bool:
    """
    Check if a word is a palindrome. By comparing if the word is the
    same backwards.
    :param string: The word that the user want to check.
    :return: True or False
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def is_palindrome_sentence(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome. Iterates through the characters
    in the centers and removes all non-alphabetical or numeric characters.

    Then compare the result backwards to see if it is a palindrome.

    :param sentence: The sentence that the user want to check.
    :return: True or False
    """
    stripped_string = ""
    for character in sentence:
        if character.isalnum():
            stripped_string += character
    return is_palindrome(stripped_string)


def fibonacci(n: int) -> int:
    """ Returns the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

