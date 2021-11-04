#         01234567890123
parrot = "Norwegian Blue"

# 在python中，字串是一種sequence type date，也就是「序列」，即由character組成的Array。
# 因此下面這行的意思就是 parrot 這個array的第3+1個字母。
print(parrot)
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

#python的序列也可以用負編號來檢索，負編號就是從序列的尾巴倒過來數
print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
print()
print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])
print()

#Slice
print(parrot[0:6])  #印出第0個字母到第5個字母(從0數到6但不包括6)
print(parrot[:6])   #若切片起點是0，則:前面可以省略
print(parrot[10:])  #若切片終點是最後一個字母，則:後面可以省略
print()

#Step 間隔取號
number = "0,123.456;789:987!654"
print(number[1:10:4])   #從1號開始，每4個號取1，直到第10號為止(不包括第10號)
print(number[1::4])     #同上，取號直到序列最尾巴
separators = number[1::4]

#語法看不懂沒關係，只是示範間隔取號什麼時候可能用到
value = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in value])

print()
