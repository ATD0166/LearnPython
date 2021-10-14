print("######Head######\n")

#                   1         2
#         01234567890123456789012345
letter = "abcdefghijklmnopqrstuvwxyz"
print(letter[::-1])   #python也可以用倒序來擷取序列，方法就是指定「每隔 -x 個」來取數

#挑戰題 in lesson 31
number = letter[16:13:-1]
print(number)
number = letter[4::-1]
print(number)
number = letter[:-9:-1]
print(number)


print("\n######Foot######")