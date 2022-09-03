import time

print(f"gm time in UTC: {time.gmtime(0)}")
# print("localtime: {0}".format(time.localtime()))
# print("localtime calling time.time: {0}".format(time.localtime(time.time())))
# print(f"time: {time.time()}")

time_here = time.localtime()

print(time_here)
print("Year:", time_here[0], time_here.tm_year)
print("Month:", time_here[1], time_here.tm_mon)
print("Day:", time_here[2], time_here.tm_mday)

print("*-*'" * 80)
# time, perf_counter, process_time and monotonic has different behavior.
# time, is using the system clock. The system clock can be manipulated during the program running.
# perf_counter have higher resolution on some system are altso monotonic can't go backwards.
# monotonic means that the time can't go backwards.
# process_time returns the time the CPU used to execute count process
from time import process_time as my_timer # not a good solution i production code. obfuscate time module.
import random

input("Press enter to start!")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop!")

end_time = my_timer()

print("Started at: " + time.strftime("%X", time.localtime(start_time)))
print("Stopped at: " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))
