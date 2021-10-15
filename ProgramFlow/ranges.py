#執行看看以下四種寫法有何不同

for i in range(1, 21):
    print("i is now {}".format(i))

print("=" * 80)

for i in range(21):
    print("i is now {}".format(i))

print("=" * 80)

for i in range(1, 21, 2):
    print("i is now {}".format(i))

print("=" * 80)

for i in range(21, 1, -2):
    print("i is now {}".format(i))


