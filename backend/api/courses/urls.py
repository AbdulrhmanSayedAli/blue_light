from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, QuizzAPIView

router = DefaultRouter()
router.register("courses", CourseViewSet, basename="courses")

urlpatterns = [
    path("", include(router.urls)),
    path("quizzes/<uuid:pk>/", QuizzAPIView.as_view()),
]
