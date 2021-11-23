from contents import pantry, recipes


def search_recipe(menu_num: str) -> list:
    """Search the recipe and retrive it's ingredient by user input.

    Args:
        menu_num (str): The number of the recipe.

    Returns:
        list: The ingredients of the recipe. Returns None if there no such thing.
    """
    if menu_num in menu_dict:
        selected_recipe = menu_dict[menu_num]
        print(f"Recipe selected : {selected_recipe}")
        result = recipes[selected_recipe]
        print(result)
        return result
    else:
        print("We don't have that recipe.")
        return None


def check_pantry(ingredients_to_check: dict) -> bool:
    """Check if pantry has enough stocks of the ingredients.

    Args:
        recipe_ingredients (dict): The ingredients needed.

    Returns:
        bool: If there are enough stocks in the pantry.
    """
    result = True
    for item, quantity_needed in ingredients_to_check.items():
        quantity_in_pantry = pantry.get(item, 0)
        if quantity_needed <= quantity_in_pantry:
            print(f"\t{item} OK")
        else:
            difference = quantity_needed - quantity_in_pantry
            add_to_shopping_list(shopping_list, item, difference)
            print(f"\tNeed to buy {difference} of {item}...")
            result = False

    return result


def consume_ingredient(recipe_ingredients: list):
    """Consume the ingredients from the pantry.

    Args:
        recipe_ingredients (list): The ingredients of the recipe.
    """
    for i in recipe_ingredients:
        pantry[i] -= 1
        if pantry[i] <= 0:
            pantry.pop(i)
    print("Ingredients left in pantry: ")
    for key, value in pantry.items():
        print(f"\t{key} = {value}")


def add_to_shopping_list(data: dict, item: str, quantity: int):
    """Adding item and it's quantity to buy into `data`.

    Args:
        data (dict): The shopping list.
        item_name (str): Items to buy.
        quantity (int): Quantity needed.
    """
    if item in data:
        data[item] = quantity
    else:
        data[item] += quantity


shopping_list = {}
menu_dict = {}
for index, key in enumerate(recipes):
    menu_dict[str(index + 1)] = key

while True:
    # Display the menu
    print("\nPlease choose your recipe")
    print("-------------------------")
    for key, value in menu_dict.items():
        print(f"{key} - {value}")
    print("0 - Exit")

    choice = input(":   ")

    if choice == "0":
        break
    else:
        ingredients = search_recipe(choice)

    if ingredients == None:
        continue

    if check_pantry(ingredients) == False:
        continue

    print("Are you sure to make this dish? (Y/N)")
    double_check = input(": ").casefold()
    if double_check == "y":
        consume_ingredient(ingredients)
        
        
print(shopping_list)
