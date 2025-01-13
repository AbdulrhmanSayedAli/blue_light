from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from phonenumber_field.serializerfields import PhoneNumberField


class LoginSerializer(serializers.Serializer):
    phone_number = PhoneNumberField(
        required=True,
        help_text=_("The phone number of the user in international format (e.g., +963932123332)."),
    )
    device_id = serializers.CharField(
        max_length=255,
        required=True,
        help_text=_("Unique device identifier."),
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        help_text=_("The user's password."),
    )

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        device_id = attrs.get("device_id")
        password = attrs.get("password")

        # Ensure all required fields are provided
        if not phone_number or not device_id or not password:
            raise serializers.ValidationError(_("Phone number, device ID, and password are required."))

        return attrs
