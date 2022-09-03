empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)

digits = sorted("432985617")
print(digits)
for digit in digits:
    digits[digits.index(digit)] = int(digit)
print(digits)

digits = list("432985617")
print(digits)

# more_numbers = list(numbers)
# more_numbers = numbers[:]
more_numbers = numbers.copy()
print(more_numbers)
print(numbers is more_numbers)
print(numbers == more_numbers)
print("Numbers ID: {}".format(id(numbers)))
print("More Numbers ID: {}".format(id(more_numbers)))
