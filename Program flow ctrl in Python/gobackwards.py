data = [104, 101, 4, 205, 308, 203, 5, 107, 307, 100, 106, 102, 108]
min_valid = 100
max_valid = 200

list_of_list = [[4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183,
                 185, 187, 188, 191],
                [104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185,
                 187, 188, 191, 350, 360],
                [104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185,
                 187, 188, 191],
                [1024, 1045, 8104, 2105, 3110, 1120, 2130, 6130, 1150,
                 3160, 2170, 3183, 1185, 4187, 5188, 6191, 7350, 1360],
                []
                ]


# iterate backwards over a sequence
# for index in range(len(data) - 1, - 1, - 1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         del data[index]

# iterate backwards over a sequence using reversed() funktion.
# this loop is slightly more efficient than the abow loop. Because the
# method enumerate() is faster than looking up data[index].

# top_index = len(data) - 1
# for index, value in enumerate(reversed(data)):
#     if value < min_valid or value > max_valid:
#         # To find which index in the data list we need to subtract the
#         # index of the reversed(data) list with the highest index in the
#         # data list.
#         print(top_index - index, value)
#         del data[top_index - index]
#
# print(data)

# testing code with a loop that lops through different tables.
test_no = 0
for list_to_test in list_of_list:
    test_no += 1
    print("------- Test no {} -------".format(test_no))
    print("list before test: {}".format(list_to_test))

    # Code to be tested is below this comment.
    top_index = len(list_to_test) - 1
    for index, value in enumerate(reversed(list_to_test)):
        if value < min_valid or value > max_valid:
            #print(top_index - index, value)
            del list_to_test[top_index - index]
    print("list  after test: {}".format(list_to_test))
    print("")

