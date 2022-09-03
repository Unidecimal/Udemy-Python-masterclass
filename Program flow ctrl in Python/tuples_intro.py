# t = ("a", "b", "c")
# print(t)
# tuples don't need parentheses but in some examples you need them.
# as in the print function, or other function when the tuple are passed
# as an argument.

# welcome = ("Welcome to my Nightmare", "Alice Cooper", 1975)
# bad = ("Bad Company", "Bad Company", 1974)
# budgie = ("Nightflight", "Budgie", 1981)
# imelda = ("More Mayhem", "Emilda May", 2011)
# metallica = ("Ride the Lightning", "Metallica", 1984)

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
# # metallica[0] = "Bölsa"
# meltallica2 = list(metallica)
# print(meltallica2)
# meltallica2[0] = "Masters of Puppets"
# print(id(metallica))
# metallica = tuple(meltallica2)
# print(metallica)
# print(id(metallica))

# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)
#
# table = ("Coffee table", 200, 100, 75, 34.50)
# print(table[1] * table[2])
#
# name, length, width, height, price = table
# print(length * width)

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

for name, artist, year in albums:
    print("Album: {}, Artist {}, Year: {}"
          .format(name, artist, year))

for album in albums:
    name, artist, year = album  # Not as sufficient but have the original album available.
    print("Album: {}, Artist {}, Year: {}"
          .format(name, artist, year))