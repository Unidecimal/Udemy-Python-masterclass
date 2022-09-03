from datetime import datetime


def create_date(date_string: str) -> datetime:
    """
    Convert a string to datetime.

    :rtype: datetime
    :param date_string: The string formatted as YYYY-MM-DD HH:MM:SSUTC
    :return: datetime: datetime object.
    """
    date_string = date_string.strip("UTC")
    format_string = "%Y-%m-%d %H:%M:%S"
    return datetime.strptime(date_string, format_string)


def is_date_time_in_range(range_string: str, check_date: datetime) -> bool:
    """
    Checks if a date is in between two dates.
    :param range_string: sting formatted as YYYY-MM-DD HH:MM:SS - YYYY-MM-DD HH:MM:SS.
    :param check_date: the date as a datetime obj.
    :return: bool
    """
    range_list = range_string.split(' - ')
    range_start = create_date(range_list[0])
    range_end = create_date(range_list[1])
    # check if the date is in range
    if range_start <= check_date <= range_end:
        return True
    else:
        return False




def create_report(data: list, range_string: str) -> dict:
    """
    Loops through the data and creates a report with 'url',
    'page views', 'visitors' for any given time range.
    :param data: the data to search
    :param range_string: The time range you are interested to search
    :return: a dict with the uniq data.
    """
    report = dict()
    # Loops over the in data
    for entry in data:
        date_to_check = entry[0]
        # if the data is in specified range extract data.
        if is_date_time_in_range(range_string, date_to_check):

            uniq_visitors = dict()  # To remember uniq visitors.
            user_visits = 0
            url = entry[1]  # the url used as a key in the report dict.
            user_id = entry[2]
            page_views = 0
            current_update = report.get(url, "No entry")

            # check if url key is in report dict
            if current_update == "No entry":
                user_visits += 1  # update user visits if there are no users.
                page_views += 1  # update page views.
                uniq_visitors.update({user_id: user_visits})
                report.update({url: (page_views, uniq_visitors)})
            else:
                # unpack the tuple
                page_views, uniq_visitors = current_update
                if user_id in uniq_visitors:
                    user_visits = uniq_visitors.get(user_id)
                    user_visits += 1
                    page_views += 1
                    uniq_visitors.update({user_id: user_visits})
                else:
                    page_views += 1
                    user_visits = 1
                    uniq_visitors.update({user_id: user_visits})
                report.update({url: (page_views, uniq_visitors)})

    return report


def read_log_file(path_to_file: str) -> list:
    """
    Reads a TXT file and returns a list with the content stripped from
    some formatting like new line and the bar character. E.g. '\n' and '|'
    :param path_to_file: like a string E.g. '/user/log.txt'
    :return: A list with content of the file in strings and datetime.
    """
    log_file_data = list()
    with open(path_to_file, 'r') as site_data:  # reads the log
        for line in site_data:
            # reading a line and striping it of '\n' and '|'
            stripped_line = line.strip('\n |')
            # splits the line.
            splitted_line = stripped_line.split(' |')
            # check so 'labels' of the tables is not added to the data.
            if not splitted_line[0].strip(' ').isalpha():
                splitted_line[0] = create_date(splitted_line[0])
                log_file_data.append(splitted_line)
    return log_file_data


def print_report(report: dict) -> None:
    """ print to console the data sorted on url names """
    # wanted to make this mor modular, but that was not prio.
    # labels
    label_table_1 = 'url'
    label_table_2 = 'page views'
    label_table_3 = 'visitors'
    print(f"|{label_table_1:<14}|{label_table_2:<11}|{label_table_3:<8}|")
    for key in sorted(report):
        views, visitors = report.get(key)
        print(f"|{key:<14}|{views:<11}|{len(visitors):<8}|")
