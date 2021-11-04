def multiply(x, y):
    result = x * y
    return result

def is_palindrome(string: str):
    backward = string[::-1]
    return backward.casefold() == string.casefold()

def palindrome_sentence(sentence: str):
    new_str = ""
    for char in sentence:
        if char.isalnum():
            new_str += char
    print(new_str)
    return is_palindrome(new_str)

word = input("Please enter a word to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome.".format(word))
else:
    print("'{}' is not a palindrome.".format(word))
    
