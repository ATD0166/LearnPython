import pathlib

create_new_paths = False

this_path = pathlib.Path(__file__)
file_path = this_path.parent.joinpath('sample.txt')

# with open(file_path, 'r') as text:
#     data = text.read()
#     print(data)

for part in this_path.parents:
    print(part)


if create_new_paths:
    unexist_path = this_path.parents[0].joinpath('new_folder')
    if not unexist_path.exists():
        unexist_path.mkdir()    # 建立該路徑

        
    unexist_file = unexist_path.joinpath('new_file.txt')
    unexist_file.touch(exist_ok=True)  #在此路徑建立檔案，exist_ok表達若檔案已存在是否覆蓋


print(str(pathlib.Path.home()))
