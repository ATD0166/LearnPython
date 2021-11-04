print("######Head######\n")

age = 4
print("Mark is " + str(age) + " years old.")     #str()是一個方法，可將()內的值轉成string type
print("Mark is {0} years old.".format(age))     #.format()是python3新增的轉型方法，用法是自動用format這個sequence內的值替換掉對應{}內的內容並轉型成.前的值的tpye

print("""
Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
""".format(28, 30, 31))

print("\n######Foot######")