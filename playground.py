def sum_eo(n, t):
    sum = 0
    if  "e" in t.casefold():
        for i in range(n):
            if i % 2 == 0:
                sum += i
    elif "o" in t.casefold():
        for i in range(n):
            if not i & 2 == 0:
                sum += i
    else:
        sum = -1
    return sum

print(
    sum_eo(
        int(input("Enter a number: ")), 
        input("Enter 'E' for even, 'O' for odd: ")
        )
    )