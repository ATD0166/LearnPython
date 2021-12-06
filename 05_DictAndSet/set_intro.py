# This is a `set`
farm_animals = {'cow', 'hen', 'horse', 'goat', 'sheep',}

# `set` is unordered
for a in enumerate(farm_animals):
    print(a)
    
more_animals = {'hen', 'horse', 'goat', 'sheep','cow',}
if farm_animals == more_animals:
    print("`farm_animals` and `more_animals` are equal")
else:
    print("`farm_animals and more_animals` are unequal")