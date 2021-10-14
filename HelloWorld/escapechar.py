print("這段話\n被分成了\n三行")
print("這段話\t被加了\t空格")
print()

# 如何在引號內把引號當成字串
print('The pet shop owner said: "No, no, \'e\'s uh,...he\'s resting".')
#or
print("The pet shop owner said: \"No, no, 'e's uh,...he's resting\".")
#or
print("""The pet shop owner said: "No, no, 'e's un,...he's resting".""")
statment = """這段話
利用三引號
分成了三行"""
print(statment)
statment = """這段話\
沒有被\
分成三行"""
print(statment)

#如何在引號內打出\n和\t等\開頭的字串
#method 1: 雙\\
print("C:\\User\\timmy\\note.txt")
#method 2: ""前加r
print(r"C:\User\timmy\note.txt")
