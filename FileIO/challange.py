# Write a program to appen the times tavle to our jabberwocky poem
# in sample.txt. We want the tables from 2 to 12 (similar to the output
# from the For loops part 2 lecture in section 6).
#
# The first column of numbers should be right justified. As an example,
# the 2 times table should look like this:
# 1 times 2 is 2
# 2 times 2 is 4

# with open("sample.txt", 'a') as tables: # append to existing file.
with open("tables.txt", 'w') as tables: # writes to a new file.
    for i in range(1, 13):
        for j in range(2, 13):
            row = "{0:2} times {1:2} is {2}".format(i, j, i * j)
            print(row, file=tables)
        print("-" * 20, file=tables)

