from rest_framework.viewsets import GenericViewSet
from .models import Rate
from rest_framework import permissions
from .serializers import RateSerializer
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework.response import Response


class RateViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    http_method_names = ["post", "get"]
    permission_classes = [permissions.IsAuthenticated]
    model = Rate
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

    def list(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def get_object(self):
        user = self.request.user
        return get_object_or_404(Rate, user=user)
