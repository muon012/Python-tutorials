print("------------------------- 1 -------------------------")
import time

print(time.gmtime(0))
print(time.localtime())
print(time.time())

time_here = time.localtime()
print("Year:", time_here.tm_year)
print("Month:", time_here.tm_mon)
print("Day:", time_here.tm_mday)
print("Hour:", time_here.tm_hour)
print("Minutes:", time_here.tm_min)
print("seconds:", time_here.tm_sec)
print("Day of the year:", time_here[7]) 