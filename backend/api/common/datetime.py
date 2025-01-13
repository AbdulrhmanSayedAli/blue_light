import datetime
import calendar
from django.utils import timezone


def get_aware_datetime_from_str(str_datetime):
    datetime_obj = datetime.datetime.fromisoformat(str_datetime)
    if datetime_obj.tzinfo is None:
        datetime_obj = timezone.make_aware(datetime_obj)
    return datetime_obj


def date_range(start_date, end_date, delta=datetime.timedelta(days=1)):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += delta


def get_nights_count(start_datetime, end_datetime):
    return (end_datetime.date() - start_datetime.date()).days


def get_all_days_between_dates(datetime_start, datetime_end):
    """
    Returns a list of all days between datetime_start and datetime_end, inclusive.

    Args:
    - datetime_start (datetime): The start datetime.
    - datetime_end (datetime): The end datetime.

    Returns:
    - List[date]: A list of days between the start and end dates.
    """
    start_date = datetime_start.date()
    end_date = datetime_end.date()

    # Get the number of days between the start and end dates
    delta = end_date - start_date

    # Generate all dates between start_date and end_date
    all_days = [start_date + datetime.timedelta(days=i) for i in range(delta.days + 1)]

    return all_days


def get_first_and_last_day_in_month(date):

    parsed_date = datetime.datetime.strptime(date, "%Y-%m")
    year = parsed_date.year
    month = parsed_date.month
    days_in_month = calendar.monthrange(year, month)[1]  # Find the number of days in the month
    first_day = datetime.datetime(year, month, 1)  # Get the first day of the month
    last_day = datetime.datetime(year, month, days_in_month)  # Get the last day of the month

    return first_day, last_day
