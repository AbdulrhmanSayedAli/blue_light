from common.audit.serializer import AuditSerializer
from users.models import City, Univeristy, Specialization, User, Experience
from common.rest_framework.serializers import CustomImageSerializerField
from django.contrib.auth.password_validation import (
    validate_password as django_validate_password,
)
from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from common.rest_framework.serializers import CustomImageSerializerField
from fcm_django.models import FCMDevice
from phonenumber_field.serializerfields import PhoneNumberField


class CitySerializer(AuditSerializer):
    class Meta:
        model = City
        fields = (
            "id",
            "name",
            "image",
        )


class UniveristySerializer(AuditSerializer):
    class Meta:
        model = Univeristy
        fields = (
            "id",
            "name",
            "image",
        )


class SpecializationSerializer(AuditSerializer):
    class Meta:
        model = Specialization
        fields = (
            "id",
            "name",
            "image",
        )


class ExperienceSerializer(AuditSerializer):
    class Meta:
        model = Experience
        fields = (
            "id",
            "text",
        )


class GetUserSerializer(AuditSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "phone_number",
            "full_name",
            "univeristy",
            "specialization",
            "city",
            "image",
            "type",
            "whatsapp",
            "about",
            "experiences",
        )

    city = CitySerializer()
    univeristy = UniveristySerializer()
    specialization = SpecializationSerializer()
    image = CustomImageSerializerField()
    experiences = ExperienceSerializer(many=True)


class RegisterSerializer(AuditSerializer):
    class Meta:
        model = User
        fields = [
            "phone_number",
            "password",
            "full_name",
            "univeristy",
            "specialization",
            "city",
            "device_id",
            "image",
        ]
        extra_kwargs = {
            "full_name": {"required": True},
            "phone_number": {"required": True},
            "device_id": {"required": True},
            "password": {"required": True},
        }

    def create(self, validated_data):
        validated_data["username"] = validated_data["device_id"]
        user = User.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        return GetUserSerializer(instance, context=self.context).data


class ProfileSerializer(AuditSerializer):
    class Meta:
        model = User
        fields = [
            "phone_number",
            "full_name",
            "univeristy",
            "specialization",
            "city",
            "image",
        ]

    image = CustomImageSerializerField(required=False, allow_null=True)

    def to_representation(self, instance):
        return GetUserSerializer(instance, context=self.context).data


class ChangePasswordSerializer(AuditSerializer):
    class Meta:
        model = User
        fields = (
            "old_password",
            "password",
        )

    old_password = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate_password(self, value):
        django_validate_password(value)
        return value

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        if validated_data["password"] == validated_data["old_password"]:
            raise serializers.ValidationError(_("New password must be different from old password."))
        user: User = self.context["request"].user
        if not check_password(validated_data.pop("old_password"), user.password):
            raise ValidationError(_("Please check your password"))
        validated_data["password"] = make_password(validated_data["password"])
        return validated_data

    def to_representation(self, user):
        return GetUserSerializer(user, context=self.context).data


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FCMDevice
        fields = ("id", "registration_id", "type", "user")
        read_only_fields = ("id", "user")


class ForgotPasswordSerializer(AuditSerializer):
    class Meta:
        model = User
        fields = (
            "phone_number",
            "device_id",
            "new_password",
        )

    phone_number = PhoneNumberField(
        required=True,
    )
    device_id = serializers.CharField(
        max_length=255,
        required=True,
    )
    new_password = serializers.CharField(
        required=True,
        write_only=True,
    )

    def validate_new_password(self, value):
        django_validate_password(value)
        return value

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number = attrs.pop("phone_number")
        device_id = attrs.pop("device_id")
        new_password = attrs.pop("new_password")

        # Ensure all required fields are provided
        if not phone_number or not device_id or not new_password:
            raise serializers.ValidationError(_("Phone number, device ID, and new_password are required."))
        attrs["password"] = make_password(new_password)
        return attrs

    def to_representation(self, user):
        return GetUserSerializer(user, context=self.context).data
