vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT65',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "Glider"

# upgrade the Virago
vehicles["virago"] = "Yamaha XV535"

del vehicles["starfighter"]
# del vehicles["f1"] this will crash
# if you use .pop without default return value, it will also crash.
result = vehicles.pop("f1", "What? This don't exist in the dict. ")
print(result)
plane = vehicles.pop("learjet", "not present")
print(plane)
bike = vehicles.pop("tenere", "not present")
print(bike)


# my_car = vehicles['fiesta']
# print(my_car)
#
# commuter = vehicles['virago']
# print(commuter)
#
# learner = vehicles.get("er5")
# print(learner)
# print(hash(learner))

hashed_vehicles = {}
for key in vehicles.keys():
    hashed_vehicles[hash(key)] = vehicles[key]

print(hashed_vehicles)

# 1st loop, less efficient than loop 2
for key in vehicles:
    print(key, vehicles[key], sep=" )) indexing--> ")

# Loop 2
for key, value in vehicles.items():
    print(key, value, sep=" )) .items()--> ")



