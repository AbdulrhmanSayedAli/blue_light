from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ADViewSet, SectionViewSet

router = DefaultRouter()
router.register("ads", ADViewSet, basename="ads")
router.register("sections", SectionViewSet, basename="sections")

urlpatterns = [
    path("", include(router.urls)),
]
