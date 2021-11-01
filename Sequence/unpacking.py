a = b = c = d = 12
print(c)

x, y, z = 1, 2, 76 # ==> This is actually a tuple
print(y)

# Unpacking a tuple
data = 1, 2, 76
print(data)
i, j, k = data
print(i)
print(j)
print(k)

# Unpacking a list
data_list = [1, 2, 76]
print(data_list)
# data_list.append(10) ==> This will cause an error
q, p, r = data_list
print(q)
print(p)
print(r)