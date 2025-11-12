# HW_01.py

import datetime


def get_days_from_today(date_str: str) -> int | str:
    """
    Calculate the difference between today's date and an arbitrary date
    in days.
    :param date_str: Date value in a 'YYYY-MM-DD' format.
    :return: Number of days (positive or negative, depending on the
    arbitrary date) or an error message.
    """
    try:
        random_date = datetime.datetime.strptime(date_str,
                                                 '%Y-%m-%d').date()
        delta_time = random_date - datetime.date.today()
        return delta_time.days
    except ValueError:
        return f'Date format should be: YYYY-MM-DD'


num_of_days = get_days_from_today('2025-11-12')
print(num_of_days)
