data = [100, 101, 4, 103, 104, 999, 105, 106, 7, 108]
min = 100
max = 200

# 方法1
# for index in range(len(data)-1, -1, -1):
#     if not min <= data[index] <= max:
#         print(index, data)
#         del data[index]
# print(data)        

# 方法2
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if not min <= value <= max:
        print(top_index - index, value)
        del data[top_index - index]
print(data)