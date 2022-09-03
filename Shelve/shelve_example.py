import shelve

"""the shelve module provides a shelve you can think of it as a dictionary 
butt stored in a file, the values can be anything that kan be pickled. The keys
must be strings. WARNING!! don use shelve-files from untrusted sources"""

# shelve is read/write by nature, so you don't need to specify the mode.
# the file is a x.db data base file. there is no shelve literal that differs from
# a dictionary.
# if you open it manually you need to remember to close it.
# fruit = shelve.open('ShelfTest')
# fruit.close()
with shelve.open('ShelfTest') as fruit:
    fruit['orange'] = "a sweet, orange , citrus fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow citrus fruit"
    fruit['grape'] = "a small, sweet fruit growing in bunches"
    fruit['lime'] = "a sour, green citrus fruit"

    # You can use del to remove data from a shelve
    # del fruit['lim']


    for key in fruit:
        print(key)

    print('=' * 40 )

    print(fruit["lemon"])
    print(fruit["grape"])
    # change a value in the shelve.
    fruit['lime'] = "great with tequila"
    for snack in fruit:
        print(snack + ": " + fruit[snack])

    # using the get method to avoid error when key isent present.
    # while True:
    #     shelf_key = input("Please enter a fruit: ")
    #     if shelf_key == "quit":
    #         break
    #     description = fruit.get(shelf_key, "We don't hava a " + shelf_key)
    #     print(description)

    # sort the output
    # print( "*=" * 80)
    # sorted_keys = list(fruit.keys())
    # sorted_keys.sort()
    #
    # for f in sorted_keys:
    #     print(f"{f} - {fruit[f]}")

    print( "*=" * 80)
    for v in fruit.values():
        print(v)

    print(fruit.values())

    for f in fruit.items():
        print(f)

    print(fruit.items())


