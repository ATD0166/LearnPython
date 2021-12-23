import time, random

sec = random.randint(5, 10)

input(
    f"""
    計時遊戲：
    在遊戲開始後，默數 {sec} 秒按下Enter，看看你猜得多準。
    
    按下Enter後開始：
    """
)

time_start = time.perf_counter()
input()
time_end = time.perf_counter()
result = time_end - time_start
diff = sec - result
print(f"你的答案是{result}秒")
if diff < 0:
    print(f"可惜，你慢了{diff.__abs__()}秒")
elif diff > 0:
    print(f"可惜，你快了{diff.__abs__()}")
else:
    print("Ｗow，完美！")
    
print()