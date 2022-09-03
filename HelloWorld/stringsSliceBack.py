letters = "abcdefghijklmnopqrstuwvxyz"


backwards = letters[::-1]  # This is a python idiom.
print(backwards)

# When slicing with negativ steps, make sure that the startvalue is greater than the stop value.

question1 = letters[16:13:-1]
print(question1)    # qpo

question2 = letters[4::-1]
print(question2)    # edcba

question3 = letters[:17:-1]
print(question3)    # zyxwvuts

# Python idioms
print(letters[::-1])    # Reverse a string
print(letters[-1:])     # Last item in a sequence
print(letters[:1])      # First item in a sequence, dosent give error if string is empty.
# not a idiom.
print(letters[0])       # Same result but can produce error if passed an empty string: string index out of range


