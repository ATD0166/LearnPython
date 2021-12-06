d = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

d2 = {
    7: 'lucky seven',
    10: 'ten',
    2: 'new two'
}

vals = d.values()
print(vals)


# Codes for "The dict `update` method" lecture.
# d.update(d2)

# for key, val in d.items():
#     print(key, val)
    
# print()

# d.update(enumerate(pantry_items))

# for key, val in d.items():
#     print(key, val)


# Code for the remaining `dict` methods lecture.
# **********************************************
# new_dict = dict.fromkeys(pantry_items, 0)
# print(new_dict)

# # .keys() 返回的是一個view-object copy, 可讀不可寫
# for item in d.keys():
#     item = 1
#     print(item)
    
# # 承上，原始dictionary的key並未真的被改動
# keys = d.keys()
# print(keys)
