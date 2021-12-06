import pathlib

file_path = pathlib.Path(__file__).parent.joinpath('sample.txt')

# with open(file_path, 'a') as sample:
#     for num in range(1,13):
#         print(f'{num} x 2 = {num * 2}', file=sample)

with open('06_IO\\sample.txt') as sample:
    contents = sample.read()
    print(contents)

