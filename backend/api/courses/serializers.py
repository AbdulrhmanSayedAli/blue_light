from common.audit.serializer import AuditSerializer
from .models import Course, CourseGroup, Video, File, Quiz, Question, Answer
from users.serializers import GetUserSerializer
from common.rest_framework.serializers import CustomImageSerializerField, CustomFileSerializerField
from rest_framework import serializers


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
            "url",
        )

    url = serializers.SerializerMethodField()
    image = CustomImageSerializerField()

    def get_url(self, instance):
        if instance.is_public:
            return instance.url
        return ""


class FullVideoSerializer(VideoSerializer):
    class Meta(VideoSerializer.Meta):
        pass

    url = serializers.URLField()


class CourseGroupSerializer(AuditSerializer):
    class Meta:
        model = CourseGroup
        fields = (
            "id",
            "name",
            "videos",
        )

    videos = VideoSerializer(many=True)


class FullCourseGroupSerializer(CourseGroupSerializer):
    class Meta(CourseGroupSerializer.Meta):
        pass

    videos = FullVideoSerializer(many=True)


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
            "file",
        )

    file = serializers.SerializerMethodField()
    image = CustomImageSerializerField()

    def get_file(self, instance):
        if instance.is_public:
            file_field = CustomFileSerializerField(use_url=True)
            file_field._context = self.context
            return file_field.to_representation(instance.file)
        return ""


class FullFileSerializer(FileSerializer):
    class Meta(FileSerializer.Meta):
        pass

    file = CustomFileSerializerField()


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


class AnswerSerializer(AuditSerializer):
    class Meta:
        model = Answer
        fields = (
            "id",
            "text",
            "is_true_answer",
        )


class QuestionSerializer(AuditSerializer):
    class Meta:
        model = Question
        fields = (
            "id",
            "text",
            "answers",
        )

    answers = AnswerSerializer(many=True)


class FullQuizSerializer(QuizSerializer):
    class Meta(QuizSerializer.Meta):
        fields = QuizSerializer.Meta.fields + ("questions",)

    questions = QuestionSerializer(many=True)


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
            "videos_price",
            "files_price",
            "quizzes_price",
            "videos_duration",
            "videos_duration_human_readable",
            "videos_count",
            "files_count",
            "quizzes_count",
            "is_buyed_files",
            "is_buyed_viedos",
            "is_buyed_quizzes",
        )

    teacher = GetUserSerializer()
    image = CustomImageSerializerField()
    groups = serializers.SerializerMethodField()
    files = serializers.SerializerMethodField()
    quizzes = QuizSerializer(many=True)
    is_buyed_files = serializers.SerializerMethodField()
    is_buyed_viedos = serializers.SerializerMethodField()
    is_buyed_quizzes = serializers.SerializerMethodField()

    def get_is_buyed_viedos(self, instance) -> bool:
        return instance.is_buyed_viedos(self.context["request"].user)

    def get_is_buyed_files(self, instance) -> bool:
        return instance.is_buyed_files(self.context["request"].user)

    def get_is_buyed_quizzes(self, instance) -> bool:
        return instance.is_buyed_quizzes(self.context["request"].user)

    def get_groups(self, instance) -> list:
        if self.get_is_buyed_viedos(instance):
            return FullCourseGroupSerializer(instance.groups, many=True, context=self.context).data
        return CourseGroupSerializer(instance.groups, many=True, context=self.context).data

    def get_files(self, instance) -> list:
        if self.get_is_buyed_files(instance):
            return FullFileSerializer(instance.files, many=True, context=self.context).data
        return FileSerializer(instance.files, many=True, context=self.context).data


# class CourseListSerializer(AuditSerializer):
#     class Meta:
#         model = Course
#         fields = (
#             "id",
#             "name",
#             "image",
#             "description",
#             "description_video",
#             "teacher",
#             "duration_in_days",
#             "price",
#             "videos_price",
#             "files_price",
#             "quizzes_price",
#             "videos_duration",
#             "videos_duration_human_readable",
#             "videos_count",
#             "files_count",
#             "quizzes_count",
#         )

#     teacher = GetUserSerializer()
#     image = CustomImageSerializerField()
