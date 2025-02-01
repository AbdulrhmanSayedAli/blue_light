from django.contrib import admin
from common.audit.admin import AuditModelAdmin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import Order, OrderCourse


class OrderCourseInline(NestedStackedInline):
    model = OrderCourse
    extra = 1
    fields = [
        "course",
        "include_videos",
        "include_files",
        "include_quizzes",
        "price",
        "expires_at",
    ]


@admin.register(Order)
class OrderAdmin(NestedModelAdmin, AuditModelAdmin):
    inlines = [OrderCourseInline]
