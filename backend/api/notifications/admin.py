from django.contrib import admin
from common.audit.admin import AuditModelAdmin
from .models import Notification


@admin.register(Notification)
class NotificationAdmin(AuditModelAdmin):
    pass
