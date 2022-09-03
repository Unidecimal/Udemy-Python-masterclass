age = int(input("How old are you?"))

# if age >= and age <= 65:
if 16 <= age <= 65:
    print("Have a good day at work.")
else:
    print("Enjoy your free time.")

print("-" * 80)

if age < 16 or age > 65:
    print("Enjoy your free time.")
else:
    print("Have a good day at work.")

print("-range-*" * 10)
# using a range insted.
if age in range(16, 66):
        print("Have a good day at work.")
else:
    print("Enjoy your free time.")
