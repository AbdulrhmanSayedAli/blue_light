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
