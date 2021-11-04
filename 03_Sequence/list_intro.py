computer_parts = ["CPU", 
                  "RAM", 
                  "SSD", 
                  "GPU", 
                  "monitor", 
                  "mother board"]

print(computer_parts)
computer_parts[3] = "trackball"     # 把list的第3個替換為"trackball"
print(computer_parts)
computer_parts[3:] = "trackball"    # 把list第3個以後的部分替換為"trackball"
                                    # 但字串在python是被定義為sequence
print(computer_parts)
computer_parts[3:] = ["trackball"]  # 同上，但這裡用[]把字串放入另一個list，
                                    # 讓python把"trackball"當成一個物件
print(computer_parts)


# print(computer_parts[0:3])
# print(computer_parts[2])
# print(computer_parts[-1])