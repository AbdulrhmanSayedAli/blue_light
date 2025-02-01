from common.audit.serializer import AuditSerializer
from .models import Course, CourseGroup, Video, File, Quiz
from users.serializers import GetUserSerializer
from common.rest_framework.serializers import CustomImageSerializerField


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


class CourseGroupSerializer(AuditSerializer):
    class Meta:
        model = CourseGroup
        fields = (
            "id",
            "name",
            "videos",
        )

    videos = VideoSerializer(many=True)


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


class QuizSerializer(AuditSerializer):
    class Meta:
        model = Quiz
        fields = (
            "id",
            "name",
            "image",
            "info",
            "info_title",
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
            "files",
            "quizzes",
            "price",
            "videos_duration",
            "videos_duration_human_readable",
            "videos_count",
        )

    teacher = GetUserSerializer()
    image = CustomImageSerializerField()
    groups = CourseGroupSerializer(many=True)
    files = FileSerializer(many=True)
    quizzes = QuizSerializer(many=True)


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
            "videos_duration",
            "videos_duration_human_readable",
            "videos_count",
        )

    teacher = GetUserSerializer()
    image = CustomImageSerializerField()
