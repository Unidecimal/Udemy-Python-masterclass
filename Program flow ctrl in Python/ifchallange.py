name = input("wat is your name: ")
age = int(input("How old are you?"))

if 18 <= age < 31:
    print("My condolences {}, you have been chosen to participate in the exclusive holidays for young people."
          .format(name))
else:
    print("{}, you are lucky to not be one of the chosen misfits that get to go on a holiday.".format(name))

