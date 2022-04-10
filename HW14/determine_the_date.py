"""
What date corresponds to the nth day of the year?
The answer depends on whether the year is a leap year or not.

Write a function that will help you determine the date if you know the number of the day in the year, as well as whether
the year is a leap year or not.
The function accepts the day number and a boolean value isLeap as arguments, and returns the corresponding date of the
year as a string "Month, day".
Only valid combinations of a day number and isLeap will be tested.
"""

import datetime


def get_day(day, is_leap):
    if is_leap and day < 367:
        date = datetime.date(4, 1, 1) + datetime.timedelta(day - 1)
    elif not is_leap and day < 366:
        date = datetime.date(1, 1, 1) + datetime.timedelta(day - 1)

    return date.strftime("%B, %d")


if __name__ == "__main__":
    assert get_day(15, False) == "January, 15"
    assert get_day(41, False) == "February, 10"
    assert get_day(59, False) == "February, 28"
    assert get_day(60, False) == "March, 01"
    assert get_day(60, True) == "February, 29"
    assert get_day(365, False) == "December, 31"
    assert get_day(366, True) == "December, 31"
