current_choice = "-"
cart = []   # create an empty list
options = ["computer",
           "monitor",
           "keyboard",
           "mouse",
           "HDMI cable",
           "SSD"]
option_nums = []
for i in range(1, len(options) + 1):
    option_nums.append(str(i))

while current_choice != "0":
    if current_choice in option_nums:
        i = int(current_choice) - 1
        chosen_item = options[i]
        cart.append(chosen_item)
        print("Adding {} into cart".format(chosen_item))
    else:
        print("Please add options from the list below:")
        for index, option in enumerate(options):
            print("{}: {}".format(index + 1, option))
        print("0: to finish")
    current_choice = input()

print("Items in your cart: ", cart)