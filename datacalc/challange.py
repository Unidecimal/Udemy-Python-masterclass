# write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter. monotonic(9 and process_time().
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.

import time

monotonic_info = time.get_clock_info('monotonic')
perf_counter_info = time.get_clock_info('perf_counter')
time_info = time.get_clock_info('time')
process_time_info = time.get_clock_info('process_time')

time_info = {'monotonic_info': monotonic_info,
             'perf_counter_info': perf_counter_info,
             'time_info': time_info,
             'process_time_info': process_time_info
             }

for info in time_info:
    about_time = time_info.get(info, "no info")
    adjustable = about_time.adjustable
    print(f"\'{info.strip('_info')}\' has the following properties: \n"
          f"Adjustable:\t\t {about_time.adjustable} \n"
          f"Implementation:\t {about_time.implementation} \n"
          f"Monotonic:\t\t {about_time.monotonic} \n"
          f"Resolution:\t\t {about_time.resolution} \n"
          "=======================================")



