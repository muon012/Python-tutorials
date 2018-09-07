print("---------------------------- 1 ----------------------------")

import pytz
import datetime

country = "US/Pacific"

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}.".format(country, local_time))
print("UTC is {}.".format(datetime.datetime.utcnow()))

print("=" * 40)

# This returns a list of all time zones.
for x in pytz.all_timezones:
	print(x)

print("=" * 40)

# This returns a list of country names.
for z in sorted(pytz.country_names):
	print(z + ": " + pytz.country_names[z])

print("---------------------------- 2 ----------------------------")

# We can get all the timezones finding the value of each country, but this will return an error when using
# "pytz.country_timezones[x]" in a for loop because "BV: Bouvet Island" doesn't have a timezone.
# We get around this problem using ".get()" instead because this returns "None" if there is no value for a key.
for y in sorted(pytz.country_names):
	print("{}: {}: {}".format(y, pytz.country_names[y], pytz.country_timezones.get(y, "No timezone")))

print("---------------------------- 3 ----------------------------")
# Getting the current time of all timezones.
for y in sorted(pytz.country_names):
	print("{}: {}".format(y, pytz.country_names[y]), end=" ==> ")
	if y in pytz.country_timezones:
		for zones in sorted(pytz.country_timezones[y]):
			tz_to_display = pytz.timezone(zones)
			local_time = datetime.datetime.now(tz=tz_to_display)
			print("\t{}: {}. ".format(zones, local_time))
	else:
		print("No timezone.")