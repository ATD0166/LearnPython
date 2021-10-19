options = [
    "Quit the game",
    "Go to the market",
    "Go to the castle",
    "Go to the lake",
    "Go to the cave",
    "Go to the guild",
    "Go back home"
]
choice = -1

while choice != 0:
    if choice not in range(0, len(options)):
        print("Please choose your next move from below: ")
        for i in range(len(options)):
            j = i + 1
            if j == len(options):
                j = 0
            print("\t{}. {}".format(j, options[j]))
    else:
        print("You {}".format(options[choice].casefold()))
    
    choice = input("Choose your next move --> ")

    while not choice.isnumeric():
        choice = input("Please enter a number: ")
    else:
        choice = int(choice)
else:
    print("Game over")    
