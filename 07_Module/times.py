import  time

# print(time.time())
# print(time.gmtime())

# time_here = time.localtime()
# print(
#     f"""
#     Year: {time_here.tm_year}
#     Mon: {time_here.tm_mon}
#     Day: {time_here.tm_mday}
#     {time_here.tm_hour}:{time_here.tm_min}:{time_here.tm_sec}
#     """
# )
# time.sleep(1)

x = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(x)
# 方向操作，字符串格式化成 time.struct_time
struct_time = time.strptime(x, "%Y-%m-%d %H:%M:%S")
print(struct_time)
    

