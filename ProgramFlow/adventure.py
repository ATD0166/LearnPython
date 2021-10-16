available_exit = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit.casefold() not in available_exit:
    chosen_exit = input("Choose a direction to leave the town: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break


print("You have gone {} and left the town".format(chosen_exit))