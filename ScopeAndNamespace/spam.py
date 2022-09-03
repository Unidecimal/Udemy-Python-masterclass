def spam1():

    def spam2():
        def spam3():
            z = " Even "
            z += y
            print("in spam3, locals are {}".format(locals()))
            return z

        y = " more " + x  # x must exist before spam3 is called
        y += spam3()  # do not combine these assignments
        print(f"In spam2, locals are {locals()}")
        return y
    x = "Spam"  # x must exist before spam2 is called
    x += spam2()  # do not combine these assignments
    print("In spam1, locals are {}".format(locals()))
    return x


def my_own_recurcive(n, rep, count=0):
    count += 1
    if count == rep:
        return n
    else:
        return n * my_own_recurcive(n+1, rep, count)

print(spam1())
print(locals())
print(globals())

for x in range(0, 11):
    print(my_own_recurcive(x, 5))
