# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

# Your code goes here ...
for item in text.casefold():  # Iterate over every character in the string.
    # Only counting letters and digits (no punctuation and other characters).
    if item.isalpha():
        # Adds item to worc_count, if w_c contains item setdefault
        # returns item and number, adds one to the number already there.
        # if item not in w_c it create key 'item' with default value 0
        # and adds 1 to itt.
        word_count[item] = word_count.setdefault(item, 0) + 1

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
