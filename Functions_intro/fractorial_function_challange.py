def factorial(number: int) -> int:
    """
    Produce a factorial number of the `int`
    :param number: The `int` to make factorial
    :return: return the product from all the values from 1 to the number.
    """
    fac_number = 1
    if number > 1:
        for i in range(2, number + 1):
            fac_number *= i
    return fac_number


for frac in range(0, 36):
    print("{0} {1}".format(frac, factorial(frac)))
