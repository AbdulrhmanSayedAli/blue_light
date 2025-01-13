from datetime import datetime
from rest_framework.exceptions import ValidationError


def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m")
    except BaseException as e:
        raise ValidationError(str(e))


def validate_full_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
    except BaseException as e:
        raise ValidationError(str(e))
