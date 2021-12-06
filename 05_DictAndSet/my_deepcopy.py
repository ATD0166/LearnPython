from contents import recipes

def my_deepcopy(dict_ori: dict) -> dict:
    """Deep copy a dictionary to a new dictionary.

    Args:
        dict_ori (dict): The dict to copy.

    Returns:
        dict: The copy of `dictionary`.
    """
    new_dict = {}
    for k, v in dict_ori.items():
        new_dict[k] = v.copy()
        
    return new_dict


recipes_copy = my_deepcopy(recipes)
recipes_copy["Pizza"]["pizza"] = 100
print(recipes["Pizza"]["pizza"])
print(recipes_copy["Pizza"]["pizza"])
