for i in range(0, 21):
    if (i != 0) and (i % 3 == 0 or i % 5 ==0):
        continue
    print(i)