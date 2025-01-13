from django.core.validators import BaseValidator
from rest_framework import exceptions


class DateTimeValidatorOnTimeChoices(BaseValidator):
    def __init__(self, choices, message="Invalid choice."):
        self.choices = choices
        self.message = message

    def __call__(self, value):
        valid_times = (valid_time for valid_time, _ in self.choices)
        if value.time() not in valid_times:
            raise exceptions.ValidationError(self.message)
