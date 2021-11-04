# Pyhton的for相當於C#的foreach
parrot = "Norwegian blue"

for character in parrot:    #此行相當於C#的"foreach (var X in parrot)"
    print(character)

print("=" * 80)

#應用例 - 拆分字串中的數字和非數字:
randomString = input("Please enter a series of number with any separators you like: ")
separators = ""

for char in randomString:
    if not char.isnumeric():
        separators = separators + char    

print(separators)

value = "".join(char if char not in separators else " " for char in randomString).split()

print(sum([int(val) for val in value]))
