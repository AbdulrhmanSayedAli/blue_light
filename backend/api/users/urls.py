from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CityViewSet,
    UniveristyViewSet,
    SpecializationViewSet,
    RegisterView,
    ChangePasswordView,
    ProfileView,
    DeviceCreateView,
    ForgotPasswordView,
    DeleteAccountView,
)

router = DefaultRouter()
router.register("cities", CityViewSet, basename="cities")
router.register("univeristies", UniveristyViewSet, basename="univeristies")
router.register("specializations", SpecializationViewSet, basename="specializations")

urlpatterns = [
    path("", include(router.urls)),
    path("register", RegisterView.as_view(), name="register"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("forgot-password/", ForgotPasswordView.as_view(), name="forgot-password"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("register-device/", DeviceCreateView.as_view(), name="register-device"),
    path("account/", DeleteAccountView.as_view(), name="delete-account"),
]
