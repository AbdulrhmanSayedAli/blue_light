from users.models import User, City, Univeristy, Specialization, Experience
from django.contrib import admin
from common.audit.admin import AuditModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from common.audit.variables import audit_fields
from django.contrib import admin, messages
from django.shortcuts import render, redirect
from django import forms
from fcm_django.models import FCMDevice
from firebase_admin import messaging


class NotificationForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    title = forms.CharField(max_length=200, required=True, initial="Admin Notification")
    message = forms.CharField(widget=forms.Textarea, required=True)


def send_custom_notification(modeladmin, request, queryset):
    if "apply" in request.POST:
        form = NotificationForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data["title"]
            message = form.cleaned_data["message"]
            devices = FCMDevice.objects.filter(user__in=queryset)
            print(title, message)
            if devices.exists():
                devices.send_message(
                    message=messaging.Message(notification=messaging.Notification(title=title, body=message))
                )
                messages.success(request, f"Notification sent to {devices.count()} device(s).")
            else:
                messages.warning(request, "No devices found for selected users.")
            return redirect(request.get_full_path())
    else:
        form = NotificationForm(initial={"_selected_action": queryset.values_list("id", flat=True)})

    return render(
        request,
        "admin/send_notification.html",
        context={"users": queryset, "form": form, "title": "Send Custom Notification"},
    )


send_custom_notification.short_description = "Send Custom Notification to Selected Users"


@admin.register(User)
class UserAdmin(BaseUserAdmin, AuditModelAdmin):
    actions = AuditModelAdmin.actions + (send_custom_notification,)
    use_list_display_getter = False
    list_display = (
        "full_name",
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
                    "full_name",
                    "phone_number",
                    "whatsapp",
                    "image",
                    "about",
                    "type",
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
