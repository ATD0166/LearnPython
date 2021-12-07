import json

random_set = {1, 3 ,5 ,7 ,9, 'apple'}

with open('set_json.json', 'w', encoding='utf8') as file:
    json.dump(random_set, file)
    
