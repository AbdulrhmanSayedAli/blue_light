from .models import Course
from .serializers import CourseSerializer, CourseListSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import permissions


class CourseViewSet(ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    model = Course
    search_fields = ["name", "teacher__full_name"]
    ordering_fields = ["name", "duration_in_days"]

    def get_queryset(self):
        queryset = Course.objects.all()
        if self.action == "retrieve":
            queryset = (
                queryset.prefetch_related("videos")
                .prefetch_related("files")
                .prefetch_related("groups")
                .select_related("teacher")
            )
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return CourseListSerializer
        return CourseSerializer
