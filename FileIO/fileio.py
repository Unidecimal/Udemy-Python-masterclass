# jabber = open("/home/melker/python_masterclass_files/sample.txt", 'r')
# jabber = open(".idea/sample.txt", 'r')
#
# for line in jabber:
#     if "jabberwock" in line.casefold():
#         print(line, end='')  #remove the dubble spacing, bara en
#
# jabber.close()

# With the 'with' it is aoutomaticlicaly tidying upp after an object is used.
# then you don't need to use the .close() funktion to prevent corrupting files.
# Even catch errors.
with open("sample.txt", 'r') as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')

print("*" * 80)
with open("sample.txt", 'r') as jabber:
    line = jabber.readline()  # readline() reads a single line and returns a sting.
    while line:
        print(line, end='')
        line = jabber.readline()

print("*" * 80)
with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()  # readlines() reads the entire file and returns a list of strings.
print(lines)

for line in lines:
    print(line, end="")

print("*" * 80)
with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end="")

print("*" * 80)
with open("sample.txt", 'r') as jabber:
    lines = jabber.read()  # read() reads the entire file and if it is a txt file returns
                         # a string kontaining the entire text.

for line in lines[::-1]:
    print(line, end="")