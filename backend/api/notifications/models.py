from django.db import models
from users.models import User
from common.audit.models import HistoricalAuditModel


class Notification(HistoricalAuditModel):
    title = models.CharField(max_length=300)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
