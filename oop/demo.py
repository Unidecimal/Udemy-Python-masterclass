a_string = "this is\na string split\t\tand tabbed"
raw_string = r"this is\na string split\t\tand tabbed"
print(a_string)
print(raw_string)

b_string = "this is" + chr(10) + "a string split" + chr(9) + chr(9) + "and tabbed"
print(b_string)

backslash_string = "tis is a backslash \followed by some text"
print(backslash_string)
backslash_string = "tis is a backslash \\followed by some text"
print(backslash_string)

error_string = r"this strin ends with \\"  # with only one \ this string will show a error.
