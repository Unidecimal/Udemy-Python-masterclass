# for index, character in enumerate("abcdefgh"):
#     print(index, character)

# below code shows that abow code just are shorthand for printing out
# a tuple that enumerate() returns.
for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)

index, character = (0, 'a')
print(index)
print(character)