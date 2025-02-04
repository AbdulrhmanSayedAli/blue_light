from .models import Course
from .serializers import CourseSerializer, CourseListSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import permissions
from .filters import CourseFilter
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action


class CourseViewSet(ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    model = Course
    search_fields = ["name", "teacher__full_name"]
    ordering_fields = ["name", "duration_in_days", "created_at"]
    ordering = ["-created_at"]
    filterset_class = CourseFilter

    def get_queryset(self):
        queryset = Course.objects.all()
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
        if self.request.method == "GET":
            return CourseSerializer

    @action(detail=True, methods=["put"], url_path="favourite")
    def toggle_favourite(self, request, pk=None):
        """Toggle the favourite status for the authenticated user on a course."""
        course = get_object_or_404(Course, pk=pk)

        if request.user in course.favourite_users.all():
            course.favourite_users.remove(request.user)
            message = "Removed from favorites."
        else:
            course.favourite_users.add(request.user)
            message = "Added to favorites."

        return Response({"message": message}, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"], url_path="my-favourites")
    def my_favourites(self, request, pk=None):
        """List all courses favorited by the authenticated user."""
        favourite_courses = Course.objects.filter(favourite_users=request.user)
        serializer = CourseListSerializer(favourite_courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
