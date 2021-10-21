# In Python, int, float, boolean, string, tuple values are immutable.
# Which means these type of values can't be changed, once they were created.

result = "String"
another_result = result
print(id(result))
print(id(another_result))

another_result = "String"
print(another_result)
print(id(another_result))

result += "_01"
print(result)
print(id(result))

another_result += "_01"
print(another_result)
print(id(another_result))

another_result = result
print(id(another_result))

print()
result += "_02"
print(another_result)
print(result)

print()
result = True
print(result)
print(id(result))
another_result = True
print(another_result)
print(id(another_result))

print()
result = 10
print(result)
print(id(result))
another_result = 10
print(another_result)
print(id(another_result))

