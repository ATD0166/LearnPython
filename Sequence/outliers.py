data = [1, 2, 150, 100, 101, 102, 103, 104, 145, 360, 361]
#data = [1, 2, 150, 100, 101, 102, 103, 104, 145]
#data = [150, 100, 101, 102, 103, 104, 145, 360, 361]
#data = [150, 100, 101, 102, 103, 104, 145]
#data = [1500, 1000, 1001, 1002, 1030, 1040, 1450]
#data = []


min = 100
max = 200

# Remove values beneath the min
stop = 0
for index, value in enumerate(data):
    if value >= min:
        stop = index
        break
print(stop)
del data[:stop]
print(data)

# Remove values above the max
start = 0
for index in range(len(data)-1, -1, -1):     # range(start, stop, 正數or倒數)
    if data[index] <= max:
        start = index + 1
        break
print(start)
del data[start:]
print(data)


# My solution
print()

data_index = 0

while data_index != len(data):
    if not min < data[data_index] < max:
        del data[data_index]
    else:
        data_index += 1
        
print(data)