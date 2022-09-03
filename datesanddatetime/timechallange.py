# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in the timezone, as
# well as local time and UTC time.
#
# Display the dates and times in a format stable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import pytz
import datetime
import random


def randomize_choices() -> dict:
    """ randomly choose 9 timezones from pytz all_timezones and return a dict """
    timezone_choices = dict()
    while len(timezone_choices) < 9:
        timezone_str = pytz.all_timezones[random.randint(0, len(pytz.all_timezones) - 1)]
        tz_to_display = pytz.timezone(timezone_str)
        timezone_time = datetime.datetime.now(tz=tz_to_display)
        timezone_choices.update({timezone_str: timezone_time})
    return timezone_choices


def make_menu(timezone_choices: dict) -> dict:
    """ Make a menu with the content of a dict, returns a dict """
    menu = dict()
    for num, zone_name in enumerate(timezone_choices.keys(), 1):
        menu.update({num: zone_name})
    return menu


def stringify_menu(menu: dict) -> str:
    """ Get a dict and make a string with its items and keys."""
    str_menu = str()
    for number in sorted(menu):
        str_menu += f"{number}: {menu.get(number)}\n"
    str_menu += "0: To quit program"
    return str_menu


def stringify_timezone_to_display(timezone: str) -> str:
    """ take a timezone and produce som time"""
    str_display = str()
    tz_to_display = pytz.timezone(timezone)
    world_time = datetime.datetime.now(tz=tz_to_display)
    str_display += "In {} \n".format(timezone)
    str_display += "World time is {} \n".format(world_time.strftime('%A %x %X %z'))
    str_display += "Local time is {} \n".format(datetime.datetime.now().strftime('%A %x %X'))
    str_display += "UTC   time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X'))
    return str_display


menu = make_menu(randomize_choices())
str_menu = stringify_menu(menu)
print(str_menu)
while True:
    choice = input(": ")
    if choice.isnumeric() and int(choice) in range(0, 10):
        if choice == '0':
            print('Quit program')
            break
        else:
            print("Your choice was {}".format(choice))
            print(stringify_timezone_to_display(menu.get(int(choice))))
    else:
        print("Please pic a choice from below menu.")
        print(str_menu)
