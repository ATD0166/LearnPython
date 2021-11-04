pangram = "The quick fox jumps over the lazy dog"

letters = sorted(pangram)
print("letters = {}".format(letters))
print("pangram = {}".format(pangram))
print()

# sorted() (函式)) vs .sort() (方法) 
numbers = [5.5, 2.2, 1.1, 4.4 ,3.3]
numbers_sorted = sorted(numbers)
print("sorted = {}".format(numbers_sorted))     #函式sorted會return值
numbers_sort = numbers.sort()
print(".sort = {}".format(numbers_sort))        #方法.sort不return任何值
print()

# 使排序無視英文字母大小寫，注意casefold不要加()
another_letter = sorted("AbCdEfGhIjK", key = str.casefold)
print(another_letter)

names = ["adam",
         "Brian",
         "cathy",
         "David",
         "elan"]
# 錯誤用法，不會印出任何東西，因為.sort方法不return值
print(names.sort())

names.sort(key = str.casefold)
print(names)
             

