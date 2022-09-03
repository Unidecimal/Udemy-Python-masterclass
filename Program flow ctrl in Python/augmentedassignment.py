X = 23

X += 1
print(X)    # 24

X -= 4
print(X)    # 20

X *= 5
print(X)    # 100

X //= 4
print(X)    # 25

X /= 5
print(X)    # 5.0 - note conversion from int to float

X **= 2
print(X)    # 25.0 - x still represents a float

X %= 5
print(X)    # 0.0 - 25 is exactly divisible by 5

greeting = "Good "
print(greeting)

greeting += "morning"
print(greeting)

greeting *= 5
print(greeting)

number = 5
multiplier = 8
answer = 0

for x in range(0, multiplier):
    answer += number
print(answer)
