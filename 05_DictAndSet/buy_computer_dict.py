available_parts = {"1":"computer",
                   "2":"monitor",
                   "3":"keyboard",
                   "4":"mouse",
                   "5":"HDMI cable",
                   "6":"SSD",
                   }

cart = {}   # create a empty dictionary
current_choice = None
while current_choice != "0":
    if current_choice in available_parts:
        if current_choice in cart:
            part = cart.pop(current_choice)
            print(f"Removing {part} from cart")
        else:
            chosen_part = available_parts[current_choice]
            cart[current_choice] = chosen_part
            print(f"Adding `{chosen_part}` into the cart.")
        print(f"Items in cart: {cart}")
    elif current_choice != "0":
        for key, part in available_parts.items():
            print(f"{key}: {part}")
        print("0: EXIT")
        
    current_choice = input("> ")
