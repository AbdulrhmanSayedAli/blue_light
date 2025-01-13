from common.audit.serializer import AuditSerializer
from users.models import City, Univeristy, Specialization, User
from common.rest_framework.serializers import CustomImageSerializerField


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
            "username",
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
            "username",
            "univeristy",
            "specialization",
            "city",
            "device_id",
            "image",
        ]
        extra_kwargs = {
            "username": {"required": True},
            "phone_number": {"required": True},
            "device_id": {"required": True},
            "password": {"required": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        return GetUserSerializer(instance, context=self.context).data
