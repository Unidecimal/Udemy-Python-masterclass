a = b = c = d = e = f = 12
print(c)
f = 42
print(c)
print(f)
a = b = c = d = e = 42
print(c)
print(c == f)

# below code is called unpacking a tuple.
x, y, z = (1, 2, 76)
print(x)
print(y)
print(z)

print("Unpacking a tuple")  # data represents a tuple
data = (1, 2, 76)
x, y, z = data
print(x)
print(y)
print(z)

print("Unpacking a list")
data_list = [12, 13, 14]
# data_list.append(15)  Problem with list is that the can change
# they are mutable tuples are immutable, so you can be sure that it is
# always the same size.
p, q, r = data_list
print(p)
print(q)
print(r)
