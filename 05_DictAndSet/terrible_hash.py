def simple_hash(key: str) -> int:
    return ord(key[0]) % 10


def get(key: str) -> str:
    address = simple_hash(key)
    return vals[address]
    

data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy"),
]   

keys = [""] * 10
vals = keys.copy()

for k, v in data:
    address = simple_hash(k)
    keys[address] = k
    vals[address] = v

test = get("apple")
print(test)
