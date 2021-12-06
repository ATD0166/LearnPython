numbers = set()

# while len(numbers) < 4:
#     number = input("Enter your next number:  ")
#     numbers.add(number)
# print(numbers)

data = ['blue', 'red', 'blue', 'yellow', 'red', 'green']

# 利用set去除資料中的重複項
unique_data = set(data)
print(unique_data)

# 利用dict.fromkey和list去除資料中的重複項，並維持原始資料排序
unique_seq_data = list(dict.fromkeys(data))
print(unique_seq_data)

    