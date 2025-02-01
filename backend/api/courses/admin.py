from django.contrib import admin
from common.audit.admin import AuditModelAdmin
from .models import Course, CourseGroup, Video, File, Quiz, Question, Answer
from nested_inline.admin import NestedTabularInline, NestedModelAdmin


class AnswerInline(NestedTabularInline):
    model = Answer
    extra = 1
    fields = ["text", "is_true_answer"]


class QuestionInline(NestedTabularInline):
    model = Question
    extra = 1
    fields = ["text"]
    inlines = [AnswerInline]


class VideoInline(NestedTabularInline):
    model = Video
    extra = 1
    fields = ["name", "url", "price"]


class CourseGroupnline(NestedTabularInline):
    model = CourseGroup
    extra = 1
    fields = [
        "name",
        "image",
    ]
    inlines = [VideoInline]


class FileInline(NestedTabularInline):
    model = File
    extra = 1
    fields = ["name", "file", "price"]


class QuizInline(NestedTabularInline):
    model = Quiz
    extra = 1
    fields = ["name", "info_title", "price"]
    inlines = [QuestionInline]


@admin.register(Course)
class CourseAdmin(NestedModelAdmin, AuditModelAdmin):
    inlines = [CourseGroupnline, FileInline, QuizInline]


@admin.register(CourseGroup)
class CourseGroupAdmin(AuditModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(AuditModelAdmin):
    pass


@admin.register(File)
class FileAdmin(AuditModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(AuditModelAdmin):
    inlines = [AnswerInline]


@admin.register(Quiz)
class QuizAdmin(NestedModelAdmin, AuditModelAdmin):
    inlines = [QuestionInline]
