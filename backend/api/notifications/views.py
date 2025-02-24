from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    model = Notification

    def get_queryset(self):
        queryset = Notification.objects.all(user=self.request.user)
        return queryset

    def get_serializer_class(self):
        return NotificationSerializer
