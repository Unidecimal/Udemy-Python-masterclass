
#         000000000011111
#         012345678901234
parrot = "Norwegian Blue"
#        -11111000000000
#         43210987654321

print(parrot[0:6])
print(parrot[-4:-2])    # Bl from -4 to -2 but not including.
print(parrot[-4:12])    # Bl same as abow.
print(parrot[-14:-5])   # Norwegian
print(parrot[-4:14])    # Blue
print(parrot[-14:-11])  # Nor
print(parrot[-4:-1])    # Blu
print(parrot[-9:-5])    # gian
print(parrot[-14:-11] + parrot[-4:-1] + parrot[-9:-5]) # NorBlugian