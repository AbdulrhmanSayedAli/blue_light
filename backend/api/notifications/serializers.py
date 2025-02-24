from common.audit.serializer import AuditSerializer
from .models import Notification


class NotificationSerializer(AuditSerializer):
    class Meta:
        model = Notification
        fields = (
            "id",
            "title",
            "body",
        )
