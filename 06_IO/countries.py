from pathlib import *

input_filename = 'country_info.txt'
input_filepath = Path(__file__).parent.joinpath(input_filename)

countries = dict()
with open(input_filepath, encoding='utf-8') as country_file:
    item_list = country_file.readline().strip('\n').split('|')
    for country in country_file:
        data = country.strip('\n').split('|')
        name, cap, code, code3, dialing, timezone, currency = data
        country_dict = {
            'name': name,
            'capital': cap,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency
        }
        countries[name.casefold()] = country_dict
       

# for key, val in countries.items():
#     print(key)
#     for k, v in val.items():
#         print(f"\t{k}: {v}")

while True:
    print('*' * 80)
    user_input = input("Please enter your country's name: ")
    if user_input.casefold() in countries:
        country = countries[user_input.casefold()]
        print(f"{country['name']}'s capital is {country['capital']}.")
    elif user_input == 'quit':
        break
    else:
        print(f"Sorry, we don't have '{user_input}' in our data :(")
    print()