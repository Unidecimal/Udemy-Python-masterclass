# Test 'The Magical Adder'
# ask user for three numbers separated with ','
# calculate a + b - c
# I added input control, but it was not necessary.
user_input = ""
valid_input = False
valid_characters = "0123456789,-"
separator = ","
minus = "-"
while valid_input != True:
    print("please enter three integers separated by ','")
    user_input = input()
    adjacent_separators = ""  # used for checking if adjacent separator.
    last_character = ""  # to know the last Char for checking separator & minus.
    not_misplaced_minus = True  # used for checking for misplaced minus.
    not_misplaced_separator = True  # used for checking for misplaced separator.
    characters_is_valid = None
    # checking if input characters are valid.
    for index, character in enumerate(user_input):
        # First check if characters are in the valid range of characters.
        if character in valid_characters:
            characters_is_valid = True
            # check if there are more than one separator.
            if character == separator and last_character == separator:
                adjacent_separators += character + last_character
            # check if separator not are placed in beginning or end of string.
            if character == separator and ((last_character == "") or (index == len(user_input) - 1)):
                not_misplaced_separator = False
            # check if minus sign are placed in the right place.
            # if the last_character not is a separator it is misplaced.
            if character == minus and last_character not in separator:
                not_misplaced_minus = False
        else:
            characters_is_valid = False
        last_character = character
    # Last check for all things is ok set valid input to True.
    # Expression 1: all characters ar valid.
    # Expression 2: No double separators.
    # Expression 3: There are separator in the input.
    # Expression 4: The minus is in the right place.
    # Expression 5: The user have entered enough input.
    # Expression 6: The separator is in the right place.
    if characters_is_valid and (len(adjacent_separators) < 2) \
        and (separator in user_input) and not_misplaced_minus \
        and (len(user_input) >= 5) and not_misplaced_separator:
        valid_input = True
input_list_str = user_input.split(",")
user_input_values = []

for value in input_list_str:
    user_input_values.append(int(value))

a = user_input_values[0]
b = user_input_values[1]
c = user_input_values[2]
answer = a + b - c
print(answer)
