low = 1
high = 1000
guess = 0
last_guess = 0
guess_times = 0
high_low = ""

print("\nWelcome to HiLo game!!!\n")
print("Please pick a number between {0} to {1} and remember it in your mind".format(
    low, high))
input("Press Enter to start the game...")

while True:
    last_guess = guess
    guess = low + (high - low) // 2
    guess_times += 1

    #當答案只剩下一種可能
    if high == low:
        print("\nThe answer must be {} , unless you cheat? \n".format(guess))
        break

    #當答案已經不可能有解
    if guess not in range(low, high + 1) or last_guess == guess:
        print("\n Hey! it's not fair, you cheat :(\n")
        break
    
    print("\tGuessing in the range of {0} to {1} ".format(low, high))
    high_low = input("My guess is {:3}. Am I right? (Enter H if it's higher, enter L if it's lower, enter C if I'm right) ".format(guess)).casefold()

    while high_low not in ['h', 'l', 'c'] or high_low == "":
        high_low = input("Please enter 'H', 'L', or'C'...").casefold()

    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    else:
        print("\n HA! I guessed the answer in {} moves! \n".format(guess_times))
        break