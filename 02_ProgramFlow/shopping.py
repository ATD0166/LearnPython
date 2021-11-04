shopping_list = ["milk", "egg", "pepper", "junk", "water", "beans"]

# continue
for item in shopping_list:
    if item == "junk":
        continue
    
    print("Buy {}".format(item))

print("=" * 80)

# break
item_to_find = "pepper"
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == "pepper":
        found_at = index
        break
    
print("Item found at position {}".format(found_at))

