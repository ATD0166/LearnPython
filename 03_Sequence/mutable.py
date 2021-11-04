# In Python, list, dict, set, Bytearray values are mutable.
# Which means these type of values can be changed after they were created.

shopping = ["egg",
            "milk",
            "bread",
            "rice",
            "junk"]

print(id(shopping))

another_shopping = shopping
print(id(shopping))

shopping += ["cookie"]
print(id(shopping))
print(id(another_shopping))

print(another_shopping)
    
print("Add toy")
another_shopping += ["toy"]
print(id(another_shopping))
print(shopping)