integer = set(range(101))
even_num = set(range(0, 101, 2))

print()
print(f"Even number is a subset of integer: {even_num.issubset(integer)}")
print(f"Integer is a superset of even numbers: {integer.issuperset(even_num)}")
print(even_num <= integer)
print(integer >= even_num)

print("*" * 50)

odd_num = set(range(1, 101, 2))
even_odd_sum = odd_num.union(even_num)
print(even_odd_sum <= integer)
print(even_odd_sum == integer)
print(even_odd_sum < integer)

print("*" * 50)

even_odd_sum.discard(0)
even_odd_sum.add(101)
print(even_odd_sum >= integer)
print(even_odd_sum <= integer)

print("*" * 50)

# isdisjoint = 完全無交集
print(even_num.isdisjoint(odd_num))
even_num.add(1)
print(even_num.isdisjoint(odd_num))

