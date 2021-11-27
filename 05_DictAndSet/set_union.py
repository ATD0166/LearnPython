# farm_animals = {"sheep", "cow", "goat", "horse", "chicken",}
# wild_animals = {"lion", "horse", "tiger", "goat", "panther", "elephant"}

# all_animals_1 = farm_animals.union(wild_animals)
# all_animals_2 = wild_animals.union(farm_animals)
# all_animals_3 = farm_animals | wild_animals
# print("all_animals_1 == all_animals_2 == all_animals_3 is "
#       f"{all_animals_1 == all_animals_2 == all_animals_3}")

from prescription_data import adverse_interactions

meds_to_watch = set()

# for interaction in adverse_interactions:
#     # meds_to_watch = meds_to_watch.union(interaction)  # This will create a new set each time.
    
#     # better use the method below:
#     # meds_to_watch.update(interaction)
#     # or
#     meds_to_watch |= interaction

# or, more efficiently:

meds_to_watch.update(*adverse_interactions)

print(sorted(meds_to_watch))
print(*sorted(meds_to_watch), sep="\n")