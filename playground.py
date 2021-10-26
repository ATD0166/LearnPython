ori_input = input("Please enter three numbers: ")
value_list = ori_input.split(",")
for i in range(len(value_list)):
    value_list[i] = int(value_list[i])
a = value_list[0]
b = value_list[1]
c = value_list[2]
print(a + b - c)