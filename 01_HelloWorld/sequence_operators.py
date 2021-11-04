print("######Head######\n")

string1 = "He's "
string2 = "probably "
stirng3 = "pining "
string4 = "for the "
string5 = "fjords."

#sequence的 + 和 *
print(string1 + string2 +stirng3 + string4 +string5)
print(string5 * 5)  #對字串執行print方法五次

#print(string5 + 5)  #Error，python的sequence data不會自動嘗試把int轉換成string

#sequence的query
today = "friday"
print("day" in today)           #True 檢查序列today中有無包含"day"這個字串
print("thur" in today)          #false
print("Arthur" in "Lanslot")    #false


print("\n######Foot######")