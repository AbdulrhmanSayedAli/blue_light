from users.models import User, City, Univeristy, Specialization, Experience
from django.contrib import admin
from common.audit.admin import AuditModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from common.audit.variables import audit_fields


@admin.register(User)
class UserAdmin(BaseUserAdmin, AuditModelAdmin):
    use_list_display_getter = False
    list_display = (
        "username",
        "image",
        "city",
        "univeristy",
        "specialization",
        "phone_number",
        "last_login",
        "is_staff",
        "is_superuser",
        *audit_fields,
    )
    use_fieldsets_getter = False
    fieldsets = (
        (
            "Personal Info",
            {
                "fields": (
                    "phone_number",
                    "whatsapp",
                    "image",
                    "about",
                )
            },
        ),
        (
            "University & Specialization",
            {
                "fields": (
                    "univeristy",
                    "specialization",
                    "city",
                )
            },
        ),
        ("Device Info", {"fields": ("device_id",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Important Dates",
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )


@admin.register(City)
class UserAdmin(AuditModelAdmin):
    pass


@admin.register(Univeristy)
class UserAdmin(AuditModelAdmin):
    pass


@admin.register(Specialization)
class UserAdmin(AuditModelAdmin):
    pass


@admin.register(Experience)
class UserAdmin(AuditModelAdmin):
    pass
