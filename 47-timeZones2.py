print("---------------------------- 1 ----------------------------")
import datetime
import pytz

localTime = datetime.datetime.now()
utcTime = datetime.datetime.utcnow()

print("Naive local time: {}.".format(localTime))
print("Naive UTC time: {}.".format(utcTime))

awareLocalTime = pytz.utc.localize(localTime)
awareUtcTime = pytz.utc.localize(utcTime)

print("Aware local time is {} in time zone: {}.".format(awareLocalTime,awareLocalTime.tzinfo))
print("Aware UTC time is {} in time zone: {}.".format(awareUtcTime,awareUtcTime.tzinfo))
