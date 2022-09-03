
#         000000000011111
#         012345678901234
parrot = "Norwegian Blue"
#        -11111000000000
#         43210987654321

print(parrot[0:14:2])   # NreinBu, starts att 0 in steps of 2.

number = "9,223,372,036,854,775,807"
print(number[1::4])     #,,,,,

number2 = "9,223;372:036 854,775;807"
separators = number2[1::4]
print(separators)     #,;: ,;
values = "".join(char if char not in separators else " " for char in number2).split()
print([int(val) for val in values])