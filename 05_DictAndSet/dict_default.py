from contents import pantry

# dict.setdefault() 會先檢查key是否存在，
# 若存在則返回value，
# 若不存在則用該方法後項設定的default value建立該key項。
chicken_quantity = pantry["chicken"]
print(f"chicken: {chicken_quantity}")

bean_quantity = pantry.setdefault("bean", 0)
print(f"bean: {bean_quantity}")

# dict.get()的功能類似，唯一差別是當key不存在時只會返回default value，而不會建立新項。
chocolate_quantity = pantry.get("chocolate", 0)
print(f"chocolate: {chocolate_quantity}")

bazooka_quantity = pantry.setdefault("bazooka", "ARE YOU MAD??")
print(f"bazooka: {bazooka_quantity}")

print()
for key, value in sorted(pantry.items()):
    print(key, value)
