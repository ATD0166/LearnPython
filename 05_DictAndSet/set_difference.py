from primes_and_squares import primes_generator, squares_generator

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(odds)
print(evens)

primes = set(primes_generator(100))
print(primes)
squares = set(squares_generator(100))
print(squares)
print()

# 以下兩者相同
print(odds.difference(primes))
print(odds - primes)
# 但與此不同(difference有順序差異)
print(primes -odds)


