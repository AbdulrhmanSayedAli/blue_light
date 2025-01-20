from common.audit.serializer import AuditSerializer
from .models import AD, Section
from courses.serializers import CourseSerializer


class ADSerializer(AuditSerializer):
    class Meta:
        model = AD
        fields = (
            "id",
            "name",
            "image",
        )


class SectionSerializer(AuditSerializer):
    class Meta:
        model = Section
        fields = (
            "id",
            "name",
            "courses",
        )

    courses = CourseSerializer(many=True)
