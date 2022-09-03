print("Today is a good day to learn Python")
print('Python is fun')
print("Python's string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")
greeting = "Hello"
name = "Melker"  # input("Please enter a name?")
# if we want a space, we can add that too
print(greeting + ' ' + name)


age = 24
print(age)

print("greeting is of type: ", type(greeting))
print("Age is of type: ", type(age))

age_in_words = "2 years"
print("Age_in_words is of type: ", type(age_in_words))

# to use variables in a string you can use f strings, beware thou they aren't backwards compatible erlyer python 3.6.
print(name + f" is {age} years old")

print(f"Pi is approximately {22 / 7:12.50f}")

pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
