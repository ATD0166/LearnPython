import colorama

def fizz_buzz(num: int) -> str:
    """Play fizz buzz.

    Args:
        num (int): The number to check.

    Returns:
        answer (str): 'fizz' if the number is divisible by 3.
        'buzz' if it's divisible by 5.
        'fizz buzz' if it's divisible by both 3 and 5.
        The number, as a string, otherwise.
    """
    if num % 15 == 0:
        num = "fizz buzz"
    elif num % 3 ==0:
        num = "fizz"
    elif num % 5 == 0:
        num = "buzz"
    
    return str(num)


next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    player_answer = input("Your go: ")
    if player_answer != correct_answer:
        print("I win! The correct answer was {}".format(correct_answer))
        break
else:
    print("Congrats, you reached {}".format(next_number))


# My solution
# for i in range(1, 101):
#     if i == 100:
#         print("Congrats, you reach {}!".format(i))
#         break
#     answer = fizz_buzz(i)
#     if i % 2 == 0:
#         if input("Your turn:  ") != answer:
#             print("The correct answer is {}. I win!".format(answer))
#             break
#     else:        
#         print(answer)
        
    

        
    