# print("------------------------- 1 -------------------------")
# # We can get the "gmt" time zone with the code below. We can also get the local time.
# # The return is a tuple. We can access that tuple in two ways. Either dot notation or index notation as in the last
# # example.
#
# import time
#
# print(time.gmtime(0))
# print(time.localtime())
# print(time.time())
#
# time_here = time.localtime()
# print("Year:", time_here.tm_year)
# print("Month:", time_here.tm_mon)
# print("Day:", time_here.tm_mday)
# print("Hour:", time_here.tm_hour)
# print("Minutes:", time_here.tm_min)
# print("seconds:", time_here.tm_sec)
# print("Day of the year:", time_here[7])
#
# print("------------------------- 2 -------------------------")
# # Creating a reaction time game.
# import random
# import time
# from time import time as my_timer
#
# input("Press enter to start: ")
#
# wait_time = random.randint(1, 6)
# time.sleep(wait_time)
# start_time = my_timer()
# input("Press Enter to stop: ")
#
# end_time = my_timer()
#
# print("Started at ", time.strftime("%X", time.localtime(start_time)))
# print("Ended at", time.strftime("%X", time.localtime(end_time)))
# print("Your reaction time was {} seconds.".format(end_time - start_time))
#
# print("------------------------- 3 -------------------------")
# # Same game as before, but now we will fix some issues and improve accuracy.
# # "perf_counter" is a more accurate function than "time" from the "time module.
# # Instead of "perf_counter" you can also use "monotonic." A clock using this function means that the time CAN'T go
# # backwards.
# # "process_time" also records elapsed time, but this is the time that the CPU takes to executing the current process.
#
# import random
# import time
# from time import perf_counter as my_timer
#
# input("Press enter to start: ")
#
# wait_time = random.randint(1, 6)
# time.sleep(wait_time)
# start_time = my_timer()
# input("Press Enter to stop: ")
#
# end_time = my_timer()
#
# print("Started at ", time.strftime("%X", time.localtime(start_time)))
# print("Ended at", time.strftime("%X", time.localtime(end_time)))
# print("Your reaction time was {} seconds.".format(end_time - start_time))
#
print("------------------------- 3 -------------------------")
# We will now make use of timezones.

import time

print("The epoch on this system starts at ", time.strftime("%c", time.gmtime(0)))
print("The current timezone is {} with an offset of {}".format(time.tzname[0], time.timezone))

if time.daylight != 0:
	print("\tDaylight Saving Time is in effect for this location.")
	print("\tThe DST timezone is ", time.tzname[1])

print("Local time is ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("UTC time is ", time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
print(time.tzname)