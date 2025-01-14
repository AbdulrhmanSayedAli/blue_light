from common.audit.serializer import AuditSerializer
from .models import Course, CourseGroup, Video, File
from users.serializers import GetUserSerializer
from common.rest_framework.serializers import CustomImageSerializerField


class CourseGroupSerializer(AuditSerializer):
    class Meta:
        model = CourseGroup
        fields = (
            "id",
            "name",
        )


class VideoSerializer(AuditSerializer):
    class Meta:
        model = Video
        fields = (
            "id",
            "name",
            "duration",
            "image",
            "group",
            "info",
            "price",
            "is_public",
        )

    image = CustomImageSerializerField()
    group = CourseGroupSerializer()


class FileSerializer(AuditSerializer):
    class Meta:
        model = File
        fields = (
            "id",
            "name",
            "pages_count",
            "image",
            "info",
            "price",
            "is_public",
        )

    image = CustomImageSerializerField()


class CourseSerializer(AuditSerializer):
    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "image",
            "description",
            "description_video",
            "teacher",
            "duration_in_days",
            "groups",
            "videos",
            "files",
            "price",
        )

    teacher = GetUserSerializer()
    image = CustomImageSerializerField()
    groups = CourseGroupSerializer(many=True)
    videos = VideoSerializer(many=True)
    files = FileSerializer(many=True)


class CourseListSerializer(AuditSerializer):
    class Meta:
        model = Course
        fields = (
            "id",
            "name",
            "image",
            "description",
            "description_video",
            "teacher",
            "duration_in_days",
            "price",
        )

    teacher = GetUserSerializer()
    image = CustomImageSerializerField()
