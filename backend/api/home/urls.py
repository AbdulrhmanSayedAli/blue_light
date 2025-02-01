from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ADViewSet, SectionViewSet, SectionViewSet, HomeAPIView

router = DefaultRouter()
router.register("ads", ADViewSet, basename="ads")
router.register("sections", SectionViewSet, basename="sections")

urlpatterns = [
    path("", HomeAPIView.as_view(), name="home"),
    path("", include(router.urls)),
]
