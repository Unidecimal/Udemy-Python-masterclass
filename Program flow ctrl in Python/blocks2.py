name = input("Please enter your name: ")
age = int(input("How old are you, {0}?".format(name)))
print(age)

# if age >= 18:
#    print("You are old enough to vote.")
#    print("Please put an X in the box.")
# else:
#    print("Please come back in {0} years.".format(18 - age))
# you can turn the statement the other way around it make no difference.
if age < 18:
    print("Please come back in {0} years.".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi.")
else:
    print("You are old enough to vote.")
    print("Please put an X in the box")