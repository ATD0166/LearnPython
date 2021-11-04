numbers = [1, 3, 2, 4, 7, 5]

# 2~4 會創造一個新的list，而1只是給原list增加一個新名字"new_numbers_1"
new_numbers_1 = numbers
new_numbers_2 = list(numbers)
new_numbers_3 = numbers[:]
new_numbers_4 = numbers.copy()
print("new_numbers_1 is numbers : {}".format(new_numbers_1 is numbers))
print("new_numbers_2 is numbers : {}".format(new_numbers_2 is numbers))
print("new_numbers_3 is numbers : {}".format(new_numbers_3 is numbers))
print("new_numbers_4 is numbers : {}".format(new_numbers_4 is numbers))
