from pathlib import Path
import data_handling

file_path = None
# ask for a file path
print("Please input a file path E.g: '/home/user/log.txt'")
# test so the path is valid.
while not Path(str(file_path)).is_file():
    file_path = input(" :")
    if not Path(str(file_path)).is_file():
        print("Not a valid path.")
# ask for a time range.
print("""Please input a time range path E.g: '2019-03-01 09:00:00 - 2019-03-02 11:59:59'
please notice you need to use the exact date format to not crash the program""")
date_range = input(" :")
# reads the file.
data_log = data_handling.read_log_file(file_path)
# creates the report.
report = data_handling.create_report(data_log, date_range)
# print report
data_handling.print_report(report)
