def collatz(num: int) -> int:
    number = int(num)
    loop = 0
    while number != 1:
        loop += 1
        if number % 2 == 0:
            number = int(number / 2)
        else:
            number = number * 3 + 1
    else:
        # print(f"{num} loops {loop} times to 1")
        return loop
    
    
# number = input('Enter a natural number:\n')
# with open('collatz_graph.txt', 'a') as text:
#     for i in range(1, 10001):
#         print(collatz(i), file=text)

max = int(input())
max_loop = 0
print()
for i in range(1, max + 1):
    new_loop = collatz(i)
    if new_loop > max_loop:
        max_loop = new_loop
        # print('|' * max_loop)
        print(max_loop)
    