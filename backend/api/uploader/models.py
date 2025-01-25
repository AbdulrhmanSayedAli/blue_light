from django.db import models
from django.contrib.auth import get_user_model
from common.audit.models import HistoricalAuditModel


User = get_user_model()


class Item(HistoricalAuditModel):
    file = models.FileField(upload_to="uploads/")
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="uploader_items",
    )
