from contents import pantry, recipes

#1 創建menu_dict
#2 用enumerate將recipes的key轉換為索引組(index, key)
#3 將轉換出的索引組加入menu_dict中
#4 將menu_dict列印成選單
#5 接收user input
#6 檢查user input是否為“0”，若為真則break while loop

menu_dict = {}
for index, key in enumerate(recipes):
    menu_dict[str(index + 1)] = key

while True:
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in menu_dict.items():
        print(f"{key} - {value}")
    print("0 - Exit")
        
    choice = input(":   ")
    
    if choice == "0":
        break
