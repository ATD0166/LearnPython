import random

def want_exit(number: str):
    return number.casefold() == exit_code


def is_valid_guess(number: str):
    if not number.isnumeric():
        print("Enter a 'NUMBER' between {0} and {1}."
              .format(min, max))
        return False
    
    if not int(number) in range(min, max + 1):
        print("The answer is between {0} and {1}."
              .format(min, max))
        return False
    
    return True
    

def give_hint(guess: int):
    if guess < answer:
        print("Guess higher (from {0} to {1})".format(guess, max))
        return (guess, max)
    
    if guess > answer:
        print("Guess lower (from {0} to {1})".format(min, guess))
        return (min, guess)
    
    print("Congrats, you win!")
    return (min, max)


def want_continue():
    print("Wanna play again? (Press Y to restart)")
    return input(">>  ").casefold() == "y"


exit_code = "q"
exit_game = False

while not exit_game:
    
    max = 100
    min = 1
    answer = random.randint(min, max)
    guess = ""
    guessed_times = 0
    
    print("/" * 100)
    print("\n*** The answer is {} ***\n".format(answer))      #TODO: Remove after testing 
    print(
        "Guess a number between {0} to {1} (Enter '{2}' to quit the game)"
        .format(min, max, exit_code)
        )
            
    while guess != answer:
        guess = input(">>  ")
        
        if want_exit(guess):
            exit_game = True
            break
        
        guessed_times += 1
        
        if is_valid_guess(guess):
            guess = int(guess)
        else:
            continue
        
        min, max = give_hint(guess)
        
    else:
        exit_game = not want_continue()
                    
print("OK, bye.")
print("/" * 100)