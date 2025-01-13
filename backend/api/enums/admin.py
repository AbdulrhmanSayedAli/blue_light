from django_celery_beat.models import (
    IntervalSchedule,
    CrontabSchedule,
    SolarSchedule,
    ClockedSchedule,
    PeriodicTask,
)
from django_celery_results.models import GroupResult, TaskResult
from django.contrib import admin
from knox.models import AuthToken

admin.site.unregister(SolarSchedule)
admin.site.unregister(ClockedSchedule)
admin.site.unregister(PeriodicTask)
admin.site.unregister(IntervalSchedule)
admin.site.unregister(CrontabSchedule)
admin.site.unregister(AuthToken)
admin.site.unregister(GroupResult)
admin.site.unregister(TaskResult)
