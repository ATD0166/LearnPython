import random

print("=" * 100)


continued = True
max = 100
min = 1
answer = 0
guess = 0
guessed_times = 0

while continued:
    
    answer = random.randint(min, max)

    print()
    print("*** The answer is {} ***".format(answer))   #TODO: Remove after testing

    guess = input("Guess a number between {0} to {1} (Enter 0 to quit the game): ".format(min, max))
    guessed_times = 1

    while True:
        # 檢查輸入的是不是數字
        if not guess.isnumeric():
            guess = input("It must be a NUMBER between {0} to {1} : ".format(min, max))
            continue
        
        # 確保guess的type是int
        guess = int(guess)
        
        # 檢查玩家是否要結束遊戲
        if guess == 0:
            continued = False
            break

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
        if int(guess) > answer:
            guess = input("Guess lower : ")
        else:
            guess = input("Guess higher : ")

        # 記錄玩家猜了幾次
        guessed_times += 1

    
    if (continued != False) and (input("Wanna play again? (Enter Y to retry): ").casefold() != "y"):
        continued = False
    
print("OK, bye!")

print("=" * 100)