import pathlib

file_path = pathlib.Path(__file__).parent.joinpath("sample.txt")

# sample = open(file_path, 'r')
# for line in sample:
#     if "jab" in line.casefold():
#         print(line, end="")
# sample.close()

# # Or a better way like this:
# with open(file_path, 'r') as sample:
#     for line in sample:
#         if 'jab' in line.casefold():
#             print(line)
# # `with` will automatically close the object

# with open(file_path, 'r') as sample:
#     line = sample.readline()
#     while line:
#         print(line)
#         line = sample.readline()

# with open(file_path, 'r') as sample:
#     lines = sample.readlines()
#     for line in lines:
#         print(line)
        
with open(file_path, 'r') as sample:
    data = sample.read()
    print(data)
        
