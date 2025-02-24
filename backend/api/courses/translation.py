from modeltranslation.translator import register, TranslationOptions
import simple_history
from .models import Course, CourseGroup, Video, File, Quiz


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = (
        "name",
        "description",
    )


simple_history.register(Course)


@register(CourseGroup)
class CourseGroupTranslationOptions(TranslationOptions):
    fields = ("name",)


simple_history.register(CourseGroup)


@register(Video)
class VideoTranslationOptions(TranslationOptions):
    fields = ("name",)


simple_history.register(Video)


@register(File)
class FileTranslationOptions(TranslationOptions):
    fields = ("name",)


simple_history.register(File)


@register(Quiz)
class QuizTranslationOptions(TranslationOptions):
    fields = ("name",)


simple_history.register(Quiz)
