from django.contrib import admin
from common.audit.admin import AuditModelAdmin
from .models import Course, CourseGroup, Video, File


@admin.register(Course)
class CourseAdmin(AuditModelAdmin):
    pass


@admin.register(CourseGroup)
class CourseGroupAdmin(AuditModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(AuditModelAdmin):
    pass


@admin.register(File)
class FileAdmin(AuditModelAdmin):
    pass
