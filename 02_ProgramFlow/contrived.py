numbers = [1, 15, 31, 66, 100]

for number in numbers:
    if number % 8 == 0:
        print("The numbers are unacceptable")
        break
else:
    print("All numbers are fine")