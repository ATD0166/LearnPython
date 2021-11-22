vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

vehicles["starfighter"] = "Lockheed F-104"
vehicles['learjet'] = "Bombardier Learjet 75"
vehicles['toy'] = "glider"

# Upgrade virago
vehicles['virago'] = 'Yamaha XV525'

print()

# 兩種從Dictionary移除項目的的方法： del & .pop()
del vehicles['starfighter']
#del vehicles['Ghost']   # 用del移除不存在的項目會報錯
result = vehicles.pop('Ghost', "Oops, you don't have this vehicle!")
print(result)

bike = vehicles.pop('tenere', "Oops, you don't have this vehicle!")
print("Delete {}".format(bike))

print()


# Less efficient, don't use this.
# for key in vehicles:
#     print(key, vehicles[key])

for key, value in vehicles.items():
    print(key, value, sep=': ')
