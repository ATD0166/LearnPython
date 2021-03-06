import random


def is_continued(number: str):
    """Check if user enter the exit code.

    Args:
        number (str): The number which user entered.

    Returns:
        booling: True if `number` is equal to exit code, False otherwise
    """
    return number.casefold() != exit_code


def is_valid_guess(number: str):
    """Check if user's input is numeric AND between min and max.

    Args:
        number (str): The number which user entered.

    Returns:
        booling: Is user's input valid or not.
    """
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
    """Compare user's guess is higher or lower than the answer and give hint.

    Args:
        guess (int): User's last guess.

    Returns:
        int: The new possible range of the answer from user's last guess.
    """
    if guess < answer:
        print("Guess higher (from {0} to {1})".format(guess, max))
        return (guess, max)

    if guess > answer:
        print("Guess lower (from {0} to {1})".format(min, guess))
        return (min, guess)

    print("Congrats, you guessed the answer in {} moves!"
          .format(guessed_times))
    return (min, max)


exit_code = "q"
continued = True

while continued:

    max = 100
    min = 1
    answer = random.randint(min, max)
    guess = ""
    guessed_times = 0

    print("/" * 100)
    # TODO: Remove after testing
    print("\n*** The answer is {} ***\n".format(answer))
    print(
        "Guess a number between {0} and {1} (Enter '{2}' to quit the game)"
        .format(min, max, exit_code)
    )

    while guess != answer:
        guess = input(">>  ")

        continued = is_continued(guess)
        if not continued:
            break

        if is_valid_guess(guess):
            guess = int(guess)
        else:
            continue

        guessed_times += 1

        min, max = give_hint(guess)

    else:
        continued = is_continued(
            input(
                "Wanna play again? (Press Q to exit)\n>>  "))

print("OK, bye.")
print("/" * 100)