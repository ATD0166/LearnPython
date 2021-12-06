import hashlib

print(hashlib.algorithms_guaranteed)
print(hashlib.algorithms_guaranteed)

python_program = """
for i in range(10):
    print(i)
"""

for i in python_program.encode('utf-8'):
    print(i, chr(i))

hash_code = hashlib.sha256(python_program.encode('utf-8'))
print()
print(hash_code.hexdigest())

