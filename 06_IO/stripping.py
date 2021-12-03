def removeprefix(string: str, prefix: str) -> str:
    """Remove the prefix of a string

    Args:
        string (str): The original string.
        prefix (str): The prefix to remove.

    Returns:
        str: The string without the prefix.
    """
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:]    # The copy of original string
    
    
def removesuffix(string: str, suffix: str) -> str:
    """Remove the suffix of a string.

    Args:
        string (str): The original string.
        suffix (str): The suffix to remove.

    Returns:
        str: The string without suffix.
    """
    if string.endswith(suffix):
        return string[:-len(suffix)]
    else:
        return string[:]


with open('.\\06_IO\\sample.txt') as sample:
    text = sample.readline().rstrip()
    print(text)
    
print(text.strip("esv'Tvsew "))

print("*" * 80)

print(removeprefix(text, "'Twa"))
print(removesuffix(text, "oves"))