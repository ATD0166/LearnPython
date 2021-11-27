from primes_and_squares import primes_generator, squares_generator

evens = set(range(0, 50, 2))
odds = set(range(1, 50, 2))

print(odds)
print(evens)

even_squares = evens.intersection(squares_generator(100))
odd_primes = odds & set(primes_generator(100))

print(f"The even squares are: {even_squares}")
print(f"The odd primes are: {odd_primes}")



