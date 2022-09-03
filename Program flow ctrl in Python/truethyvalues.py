if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")
# if name != "":  This is more obvious and may be better to do in the beginning.
if name:
    print("Hello, {}".format(name))
else:
    print("Are you a person without no name?")