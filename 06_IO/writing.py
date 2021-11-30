import pathlib

cities = ['Taipei', 'Tokyo', 'London', 'Paris', 'Berlin']

file_name = "cities.txt"
file_path = pathlib.Path(__file__).parent.joinpath(file_name)

# write mode下python會自己新建檔案，不需要下面程式碼
# if not file_path.exists:
#     file_path.touch()

with open(file_path, 'w') as city_file:
    for city in cities:
        print(city, file=city_file)

with open(file_path) as city_file:
    line = city_file.readline()
    while line:
        print(line, end="")
        line = city_file.readline()
