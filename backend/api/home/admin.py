from django.contrib import admin
from common.audit.admin import AuditModelAdmin
from .models import AD, Section


@admin.register(AD)
class ADAdmin(AuditModelAdmin):
    pass


@admin.register(Section)
class SectionAdmin(AuditModelAdmin):
    pass
