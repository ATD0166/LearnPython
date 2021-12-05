import pathlib

data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

file_name = "flowers.txt"
folder_path = pathlib.Path(__file__).parent
file_path = folder_path.joinpath(file_name)

# write mode下python會自己新建檔案，不需要下面程式碼
# if not file_path.exists:
#     file_path.touch()

with open(file_path, 'w') as plants:
    for flower in data:
        print(flower, file=plants)

# with open(file_path, 'w') as plants:
#     for f in data:
#         plants.write(f)
        
with open(folder_path.joinpath('writting_test.txt'), 'w') as test:
    for i in range(10):
        # test.write(i)   # Error, 因txt檔案只能寫入str
        print(i, file=test)     # print函式則預設執行'__str__'方法，會把輸出轉成str
        test.write(i.__str__()) # 如左


        
