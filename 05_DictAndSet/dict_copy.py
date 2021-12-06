import copy

animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": "cuddly",
    "pig": ["fat", "cute"]
}

things = {}

# 完全不用.copy()：reference copy
things = animals
animals["teddy"] = "toy"
print(things["teddy"])

# 使用shallow copy：淺層value copy，只複製第一層，第二層以下仍用reference copy
# things = animals.copy()

# 使用deep copy：深層value copy，會進入dict裡面的sequence也做value copy
things = copy.deepcopy(animals)

animals["lion"] = "big cat"
print(things["lion"])

things["pig"].append("smart")
print(id(animals["pig"]), animals["pig"])
print(id(things["pig"]), things["pig"])