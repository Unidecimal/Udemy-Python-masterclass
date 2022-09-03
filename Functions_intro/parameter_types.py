# p1, p2 = 2 positional or keyword arguments.
# *args = a var positional parameter.
# k = is a keyword argument it has to be passed with a key word.
# otherwise, it will be included in the var positional parameter.
# **kwargs = var keyword parameter.
def func(p1, p2, *args, k, **kwargs):
    print("Positional-or-keyword:...{},{}".format(p1, p2))
    print("var-positional (*args):..{}".format(args))
    print("keyword:.................{}".format(k))
    print("var-keyword (**kwargs):..{}".format(kwargs))


func(1, 2, 3, 4, 5, 9, k=6, key1=7, Key2=8)