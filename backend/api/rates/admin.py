from django.contrib import admin
from common.audit.admin import AuditModelAdmin
from .models import Rate


@admin.register(Rate)
class RateModelAdmin(AuditModelAdmin):
    pass
