low = 1
high = 1000
guess = 0
last_guess = 0
moves = 0
high_low = ""

print("\nWelcome to HiLo game!!!\n")
print(
    "Please pick a number between {0} to {1} and remember it in your mind"
    .format(low, high)
    )
input("Press Enter to start the game...\n")

while high != low:  #當答案只剩下一種可能
    last_guess = guess
    guess = low + (high - low) // 2
    moves += 1

    #當答案已經不可能有解
    if guess not in range(low, high + 1) or last_guess == guess:
        print("\nHey! it's not fair, you cheated :(\n")
        break
    
    high_low = input(
        "My guess is {:3}, right? "
        "(Enter H if it's higher, L if it's lower, C if I'm right) "
        .format(guess)).casefold()

    while high_low not in ['h', 'l', 'c'] or high_low == "":
        high_low = input("Please enter 'H', 'L', or'C'...").casefold()

    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    else:
        print(
            "\nHA! I guessed the answer in {} moves!\n"
            .format(moves)
            )
        break
#如果這個while loop以正常方式結束(非透過break結束)則執行
else:
    print(
        "\nThe answer must be {}, unless you cheated? "
        .format(guess)
        )
    print("I got it in {} moves\n".format(moves))