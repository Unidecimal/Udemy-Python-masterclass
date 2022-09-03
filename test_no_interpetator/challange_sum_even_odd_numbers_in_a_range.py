# Write a function named sum_eo with the following parameters.
# n: Positive number
# t: str

# if t has the value e the function should return the sum of all even natural
# numbers less than n.

# Else if t has the value o the function should return the sum of all odd
# natural numbers less than n.

# for any other values of t return -1

def sum_eo(n, t):
    sum_even_num = 0
    sum_odd_num = 0
    for nat_num in range(n):
        if (nat_num % 2) == 0:
            sum_even_num += nat_num
        else:
            sum_odd_num += nat_num
    if t.casefold() == "e":
        return sum_even_num
    elif t.casefold() == "o":
        return sum_odd_num
    else:
        return -1

    # def sum_eo(n, t):
    #     """Sum even or odd numbers in range.
    #
    #     Return the sum of even or odd natural numbers, in the range 1..n-1.
    #
    #     :param n: The endpoint of the range. The numbers from 1 to n-1 will be summed.
    #     :param t: 'e' to sum even numbers, 'o' to sum odd numbers.
    #     :return: The sum of the even or odd numbers in the range.
    #             Returns -1 if `t` is not 'e' or 'o'.
    #     """
    # if t == "e":
    #     start = 2
    # elif t == 'o':
    #     start = 1
    # else:
    #     return -1
    #
    # return sum(range(start, n, 2))


x = sum_eo(11, 'spam')
print(x)



print(sum_eo(10, "e"))
print(sum_eo(7, "o"))
print(sum_eo(11, "spam"))