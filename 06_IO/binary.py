import pathlib

file_path = pathlib.Path(__file__).parent.joinpath('binary')

# with open(file_path, 'bw') as b_file:
#     # for i in range(17):
#     #     b_file.write(bytes([i]))
#     b_file.write(bytes(range(17)))
        
# with open(file_path, 'br') as b_file:
#     for b in b_file:
#         print(b)

a = 65534   # = FF FE
b = 65535   # = FF FF
c = 65536   # = 00 01 00 00
x = 2998302 # = 00 2D C0 1E

with open(file_path, 'bw') as b_file:
    b_file.write(a.to_bytes(2, 'big'))
    b_file.write(b.to_bytes(2, 'big'))
    b_file.write(c.to_bytes(4, 'big'))
    b_file.write(x.to_bytes(4, 'big'))
    b_file.write(x.to_bytes(4, 'little'))
    
with open(file_path, 'br') as b_file:
    a_bin = int.from_bytes(b_file.read(2), 'big')
    print(a_bin)
    b_bin = int.from_bytes(b_file.read(2), 'big')
    print(b_bin)
    c_bin = int.from_bytes(b_file.read(4), 'big')
    print(c_bin)
    x_bin = int.from_bytes(b_file.read(4), 'big')
    print(x_bin)
    x_bin_2 = int.from_bytes(b_file.read(4), 'big')
    print(x_bin_2)  # 示範若把位元組端序(big / little)弄反會發生什麼事
