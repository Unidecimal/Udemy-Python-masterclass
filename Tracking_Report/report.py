import sys
import data_handling


def main() -> None:
    """Entrypoint of program."""

    args = read_args()
    file_path = args.get("file path")
    date_range = args.get("date range")

    # reads the file.
    data_log = data_handling.read_log_file(file_path)
    # creates the report.
    report = data_handling.create_report(data_log, date_range)
    # print report
    data_handling.print_report(report)


def read_args() -> dict:
    """ Check for valid CLI arguments and return them in a dictionary. """
    # note, it would be nice to improve with test for file path and date range.
    if len(sys.argv) != 3:
        print("Usage: python3 report.py [file] [date range]")
        exit()
    if len(sys.argv[2]) != 41:
        print("Date range is written as e.g: '2019-03-01 09:00:00 - 2019-03-02 12:59:59'")
        exit()
    args = {"file path": sys.argv[1], "date range": sys.argv[2]}
    return args


if __name__ == "__main__":
    main()
