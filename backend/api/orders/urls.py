from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, CheckCouponView

router = DefaultRouter()
router.register("", OrderViewSet, basename="orders")

urlpatterns = [
    path("", include(router.urls)),
    path("check-coupon/<str:code>/", CheckCouponView.as_view(), name="check-coupon"),
]
