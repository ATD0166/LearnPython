menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

# Solution 1
print("Solution 1 result: ")
for meal in menu:
    top_index = len(meal) - 1
    for index, value in enumerate(reversed(meal)):
        if value == "spam":
            del meal[top_index - index]
    print(", ".join(meal))
print()

# Solution 2
# print("Solution 2 result: ")
# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item, end=", ")
#     print()