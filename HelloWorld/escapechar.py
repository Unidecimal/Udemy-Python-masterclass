split_string = "This string has been\nsplit over\nseveral\nlines"
print(split_string)

tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string)

print('The pet shop owner said "No, no, \'e\'s u,...he\'s resting".')
#or
print("The pet shop owner said \"No, no, 'e's u,...he's resting\".")
#or with """ at the start and end of the string.
print("""The pet shop owner said "No, no, \
'e's u,...he's resting".""")
#a other use of """ if you want a string spanning over mutiple lines.
another_splitString = """This string has 
split over
several
lines"""

print(another_splitString)

# you can use \ to escape end of line as below

escape_another_splitString = """This string has \
split over \
several \
lines, but are using \\ to escape line break"""

print(escape_another_splitString)
# adding \'s in a string
print("C:\\Users\\timbuchalka\\notes.txt")
# or using a raw string using "r", raw strings are used for regex (regular expressions)
print(r"C:\Users\timbuchalka\notes.txt")

