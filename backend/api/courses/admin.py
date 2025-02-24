from django.contrib import admin
from common.audit.admin import AuditModelAdmin
from .models import Course, CourseGroup, Video, File, Quiz, Question, Answer
from nested_inline.admin import NestedModelAdmin, NestedStackedInline


class AnswerInline(NestedStackedInline):
    model = Answer
    extra = 1
    fields = ["text", "is_true_answer"]


class QuestionInline(NestedStackedInline):
    model = Question
    extra = 1
    fields = ["text"]
    inlines = [AnswerInline]


class VideoInline(NestedStackedInline):
    model = Video
    extra = 1
    fields = ["name_en", "name_ar", "url", "price"]


class CourseGroupnline(NestedStackedInline):
    model = CourseGroup
    extra = 1
    fields = [
        "name_en",
        "name_ar",
        "image",
    ]
    inlines = [VideoInline]


class FileInline(NestedStackedInline):
    model = File
    extra = 1
    fields = ["name_en", "name_ar", "file", "price"]


class QuizInline(NestedStackedInline):
    model = Quiz
    extra = 1
    fields = ["name_en", "name_ar", "info_title", "price"]
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
