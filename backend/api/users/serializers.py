from common.audit.serializer import AuditSerializer
from users.models import City, Univeristy, Specialization, User
from common.rest_framework.serializers import CustomImageSerializerField
from django.contrib.auth.password_validation import (
    validate_password as django_validate_password,
)
from rest_framework import serializers
from django.contrib.auth.hashers import check_password
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password


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
        )

    city = CitySerializer()
    univeristy = UniveristySerializer()
    specialization = SpecializationSerializer()
    image = CustomImageSerializerField()


class RegisterSerializer(AuditSerializer):
    class Meta:
        model = User
        fields = [
            "phone_number",
            "device_id",
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
