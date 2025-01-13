import re
from django.core.exceptions import ValidationError


class CustomPasswordValidator:
    def validate(self, password, user=None):
        # Regex to allow only English letters, numbers, and common special characters
        if not re.match(r'^[A-Za-z0-9!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]+$', password):
            raise ValidationError(
                "Password can only contain English letters, numbers, and special characters.",
                code="password_invalid",
            )

    def get_help_text(self):
        return "Your password can only contain English letters, numbers, and special characters."
