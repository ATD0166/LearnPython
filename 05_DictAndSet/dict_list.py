available_parts = {"1":"computer",
                   "2":"monitor",
                   "3":"keyboard",
                   "4":"mouse",
                   "5":"HDMI cable",
                   "6":"SSD",
                   }

cart = []   # Create a empty list
current_choice = None
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if chosen_part in cart:
            cart.remove(chosen_part)
            print(f"Removing `{chosen_part}` from cart.")
        else:
            cart.append(chosen_part)
            print(f"Adding `{chosen_part}` into cart.")
    elif current_choice != "0":
        for key, part in available_parts.items():
            print(f"{key}: {part}")
        print("0: EXIT")
        
    current_choice = input("> ")
