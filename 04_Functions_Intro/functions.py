def multiply(x, y):
    """Multiply 2 numbers

    Args:
        x (int): The first number
        y (int): The second number

    Returns:
        int: The result of x multiply y.
    """
    result = x * y
    return result


def is_palindrome(string: str):
    """Check if a string is a palindrome.

    Args:
        string (str): The string to check.

    Returns:
        booling: True if `string` is a palindrome, False otherwise.
    """
    backward = string[::-1]
    return backward.casefold() == string.casefold()


def palindrome_sentence(sentence: str):
    new_str = ""
    for char in sentence:
        if char.isalnum():
            new_str += char
    print(new_str)
    return is_palindrome(new_str)


def fibonacci(n):
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n
    
    n_minus1, n_minus2 = 1, 0
    
    result = None
    for i in range(n - 1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result
    
    return result
    

for i in range(20):
    print(fibonacci(i))

print(fibonacci(-1))