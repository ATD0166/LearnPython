def sum_numbers(*numbers: float) -> float:
    """Calculate the sum of a series of numbers.
    
    Arg:
        numbers (float): The numbers to calculate.

    Returns:
        float: The sum of numbers.
    """
    sum = 0
    for num in numbers:
        sum += num
        
    return sum


print(sum_numbers(132, 13.993))