# enumerate() function
# Returns 2 values: object's index(int) and object itself
for index, character in enumerate("abcdefg"):
    print(index, character) 
    
    
for t in enumerate("abcdefg"):
    index, value = t
    print(t) # This is actually a tuple
    print(index, value)
    
index, value = (0, "a")
print(index)
print(value)