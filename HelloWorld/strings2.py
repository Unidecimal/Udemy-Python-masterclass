parrot =  "Norwegian Blue"

print(parrot)

print(parrot[3])
sum = ""
for i in range(0, len(parrot)):
    sum = sum + parrot[i]
    print(sum)

print(parrot[3] + "\n" + parrot[4] + "\n" + parrot[9] + "\n" + parrot[3] + "\n" + parrot[6] + "\n" + parrot[8])
print()
print(parrot[-11] + "\n" + parrot[-10] + "\n" + parrot[-5] + "\n" + parrot[-11] + "\n" + parrot[-8] + "\n" + parrot[-6])
print()
print(parrot[3 - 14] + "\n" + parrot[4 - 14] + "\n" + parrot[9 - 14] + "\n" + parrot[3 - 14] + "\n" + parrot[6 - 14] +
      "\n" + parrot[8 - 14])
# Slice
print(parrot[0:6])      # Norweg, up to but not including index 6.
print(parrot[3:5])
print(parrot[0:9])      # including start value index 0
print(parrot[:9])       # Not including Python default index 0 of the sequence.
print(parrot[10:])      # Blue, python default to the lengt of the sequence.
print(parrot[6:])       # start index 6 to end of string
print(parrot[:6])       # Start of sting to index 6 but not inqluded.
print(parrot[:])        # start at beg, extend to end.
print(parrot[:6] + parrot[6:])

theAlphabeth = "abcdefghijklmnopqrstuvxyz"
startIndex = input("Write a number between 1 to 25!")
endIndex = input("Write a number between 1 to 25!")
print(theAlphabeth[int(startIndex)-1:int(endIndex)])






