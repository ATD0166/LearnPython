panagram = """The quick
fox\tjumped
over the lazy dog"""

print(panagram.split())

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
values = "".join(generated_list)
print(values)

value_list = values.split()
print(value_list)

print()

# Use a for loop to produce a list of ints, rather than strings.
# You can either modify the contents of the 'values_list' list in place,
# or create a new list of ints.

# 錯誤作法：
# for v in value_list:
#     v = int(v)

# 正確作法：
for i in range(len(value_list)):
    value_list[i] = int(value_list[i])
print(value_list)

# or
num_list = []
for val in value_list:
    num_list.append(int(val))
print(num_list)

