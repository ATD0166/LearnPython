numbers = (0, 1, 2, 3, 4, 5)

# * == unpack sequences

# *的第一種用法：unpack sequences
print(numbers, sep=';')
print(*numbers, sep=';')

# *的第二種用法：pack sequences
def test_star(*args):
    print(args)
    for i in args:
        print(i)
        

test_star(0, 1, 2, 3, 4, 5)

print()
test_star()
