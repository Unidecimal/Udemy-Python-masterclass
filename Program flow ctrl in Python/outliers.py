data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185,
        187, 188, 191, 350, 360]

# Testing for corner cases and
#
# print("Test 1: no high values")
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185,
#         187, 188, 191]
# print("Test 2: no lo values")
# data = [104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]
# print("Test 3: no high or low values")
# data = [104, 105, 110, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191]
# print("Test 4: no values")
# data = []
# print("Test 5: extreme high values")  # Fail
# data = [1024, 1045, 8104, 2105, 3110, 1120, 2130, 6130, 1150, 3160, 2170, 3183, 1185, 4187, 5188, 6191, 7350, 1360]


# del data[0:2]
# print(data)
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200

# not_valid_indexes = [] (for my solution)

# My try to remove values safly from a table, not to efficient with two loops.
# I comment out this and what the teacher have to say.
# for index, value in enumerate(data):
#     # find indexes of the out of range values.
#     if (value < min_valid) or (value > max_valid):
#         not_valid_indexes.append(index)
# # iterate backwards to del values that are out of range.
# for value in range(len(not_valid_indexes) - 1, -1, -1):
#     del data[not_valid_indexes[value]]
#
# print("The new list: {}".format(data))

# process the low values in the list.
print(data)
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)  # for debugging
del data[:stop]
# processing the high values in the list
start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= max_valid:
        # we have the index of the last item to keep.
        # set 'start' to the position of the first
        # item to delete, which is 1 after 'index'.
        start = index + 1
        break
print(start)
del data[start:]
print(data)

# the teachers' solution doesn't take care of deviation in the data that
# appears in the middle of the data range. He will make another video
# for that solution.
