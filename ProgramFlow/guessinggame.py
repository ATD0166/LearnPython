answer = 5
guess = int(input("Guess a number between 1 to 10: "))

while guess < 0 or guess > 10:
    guess = int(input("Sorry, the number must between 1 to 10: "))

chance = 2
while chance > 0:    
    if guess == 5:
        print("Congrats, you guessed the answer in first time!")
        chance = 0
    else:        
        if guess < 5:
            print("Guess higher")
        else:
            print("Guess lower")        
        guess = int(input("Try again? You have {} chances left :".format(chance)))
        chance = chance - 1
        if guess != 5:
            print("Too bad, still not right, out of chances...")
        else:
            print("Correct!")
