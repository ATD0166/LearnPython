import random

print("=" * 100)

max = 100
min = 1
answer = 0
guess = ""
guessed_times = 0

while True:
    
    answer = random.randint(min, max)

    print()
    print("*** The answer is {} ***".format(answer))   #TODO: Remove after testing

    guess = input("""Guess a number between {0} to {1} (Enter "Q" to quit the game): """.format(min, max))
    guessed_times = 1

    while True:
        # 檢查玩家是否要結束遊戲
        if guess.casefold() == "q":
            guess = "q";
            break
        
        # 檢查輸入的是不是數字，確保guess的type是int
        if guess.isnumeric():
            guess = int(guess)
        else:
            guess = input("It must be a NUMBER between {0} to {1} : ".format(min, max))
            continue
        
        # 檢查輸入範圍是否符合遊戲規則
        if guess not in range(min, max + 1):
            guess = input("The number must between {0} to {1} : ".format(min, max))
            continue
        
        # 檢查玩家有無猜對
        if guess == answer:
            if guessed_times <= 1:
                print("Congrats, you guessed the answer in first time!")
            else:
                print("Correct! you guessed the answer in {} times".format(guessed_times))
            break
        
        # 檢查玩家猜得太高還太低
        if guess > answer:
            guess = input("Guess lower : ")
        else:
            guess = input("Guess higher : ")

        # 記錄玩家猜了幾次
        guessed_times += 1
    
    if (guess == "q") or (input("""Wanna play again? (Enter "Y" to start a new game): """).casefold() != "y"):
        print("OK, bye!")
        break    

print("=" * 100)