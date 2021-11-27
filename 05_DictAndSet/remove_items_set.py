small_ints = set(range(21))
print(small_ints)
print()
# Two ways to remove a item from a set:
# 1. .discard()
small_ints.discard(10)
print(small_ints)
# 2. .remove()
small_ints.remove(11)
print(small_ints)
print()
# using .discard() to remove a noneexist item won't raise error.
small_ints.discard(99)
print(small_ints)
# but .remove() will.
small_ints.remove(99)
print(small_ints)