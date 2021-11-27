# There can be multi-intersections
binaries = set(range(0, 500, 2))
decimals = set(range(0, 500, 10))
hexes = set(range(0, 500, 16))

common_multiple_1 = binaries & decimals & hexes
print(common_multiple_1)
# or
common_multiple_2 = binaries.intersection(decimals, hexes)
print(common_multiple_1 == common_multiple_2)
