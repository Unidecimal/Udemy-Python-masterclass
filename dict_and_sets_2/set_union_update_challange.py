scorpions = {"emperor", "red claw", "arizona", "forest", "fat tail"}
snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spiders = {"tarantula", "black widow", "wolf spider", "crab spider"}
vespas = {"yellowjacket", "hornet", "paper wasp"}

# Create a set of things that bite or things that sting. Spiders bite,
# scorpions and vespas sting.

stingers = scorpions | vespas
biters = snakes | spiders

print(f"Things that bites {biters}")
print(f"Things that stings {stingers}")

arachnids = scorpions.union(spiders)
print("Arachnids: {0}".format(arachnids))

