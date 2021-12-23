import pytz
import datetime

tz_set = pytz.all_timezones_set.copy()
tz_dict = dict()
for i in range(9):
    tz_dict[str(i + 1)] = tz_set.pop()
tz_dict['0'] = 'Quit'

while True:
    # step 1: show tz_list
    print()
    for key, tz in tz_dict.items():
        print(f"{key}. {tz}")

    # step 2: get user input
    print()
    user_input = input(
        "Enter a number to show the localtime and UTC time of the timezone\n>> ")

    # step 3: check if quit or not
    if user_input == '0':
        print('Goodbye!')
        break
    
    # step 4: check if input valid
    if tz_dict.get(user_input) == None:
        print(f"Sorry, {user_input} is not a valid option...")
        continue

    # step 5: transfer user-input to tz_info
    tz_info = pytz.timezone(tz_dict[user_input])

    # step 6: use input to search item in datetime module.
    localtime = datetime.datetime.now(tz=tz_info)
    utctime = datetime.datetime.utcnow()
    print(f"\nThe time in {tz_dict[user_input]} is\n\n {localtime.strftime('%A, %x, %X')}")
    print(f"\nThe UTC time is\n\n {utctime.strftime('%A, %x, %X')}")
    
    input("\nPress enter to continue...")