fighters = {
    'raptor': 'F-22',
    'eagle': 'F-15',
    'falcon': 'F-16',
    'tomcat': 'F-14',
    'tiger-fish': 'F-5',
    'phantom': 'F-4',
    'lightning': 'F-23',
    'hornest': 'F-18'
}

# Less efficient, don't use this.
# for key in fighters:
#     print(key, fighters[key])

for key, value in fighters.items():
    print(key, value)
