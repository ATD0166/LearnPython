def factorial(number: int) -> int:
    """Calculate the factorial of a number.

    Args:
        number (int): The number to calculate.

    Returns:
        int: The factorial of `number`
    """
    result = 1
    if str(number).isnumeric():
        number = int(number)
        for i in range(1, number + 1):
            result *= i
    else:
        raise TypeError("The parameter `number` must be an positive integer")
    
    return result


for i in range(36):
    print("{0} {1}".format(i, factorial(i)))