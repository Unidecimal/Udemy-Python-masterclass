def sum_numbers(*numbers: float) -> float:
    """
    Takes a numbers of numbers and sum them upp.
    :param numbers: the numbers to be summed upp.
    :return: the sum of all numbers
    """

    sum_num = 0
    for num in numbers:
        sum_num += num
    return sum_num


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
