# farm_animals = {"Cow", "Pig", "Sheep", "Hen", "Horse", "Goat"}
# wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse", "pig"}
#
# all_animals_1 = farm_animals.union(wild_animals)
# print(all_animals_1)
#
# all_animals_2 = wild_animals.union(farm_animals)
# print(all_animals_2)
#
# all_animals_3 = wild_animals | farm_animals
# print(all_animals_3)

from prescription_data import adverse_interactions

meds_to_watch = set()
# for interaction in adverse_interactions:
#     # meds_to_watch = meds_to_watch.union(interaction)
#     # meds_to_watch = meds_to_watch | interaction
#     # meds_to_watch.update(interaction)
#     meds_to_watch |= interaction

# you can do the same as the for loop with the * arg. That is becous
# of the union funcrion have the *others. You unpack all sets in
# adverse_interactions and update the meds_to_watch
meds_to_watch.update(*adverse_interactions)


print(sorted(meds_to_watch))
print(*sorted(meds_to_watch), sep="\n")
