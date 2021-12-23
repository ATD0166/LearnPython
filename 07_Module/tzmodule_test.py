import pytz, datetime

location = 'Europe/Moscow'
timezone = pytz.timezone(location)
localtime = datetime.datetime.now(tz=timezone)

print()
print(f"The time in your aria is {datetime.datetime.now()}")
print(f"The time in {location} is {localtime}.")
print(f"UTC is {datetime.datetime.utcnow()}")
print()

for country, tz in pytz.country_timezones.items():
    print(f"{pytz.country_names[country]}: ")
    for zone in sorted(tz):
        tz_info = pytz.timezone(zone)
        local_time = datetime.datetime.now(tz=tz_info)
        print(f"\t{zone}...{local_time}")

print()

