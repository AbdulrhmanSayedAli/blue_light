from rest_framework import routers
from .views import (
    UserTypeReadOnlyViewSet,
    PaymentStatusReadOnlyViewSet,
)


router = routers.DefaultRouter()

# router.register("os-types", OsTypeReadOnlyViewSet, "os-types")
# router.register("gender", GenderReadOnlyViewSet, "gender")
# router.register(
#     "notification-object-type",
#     NotificationObjectTypeReadOnlyViewSet,
#     "notification-object-type",
# )
# router.register(
#     "notification-template-type",
#     NotificationTemplateTypeReadOnlyViewSet,
#     "notification-template-type",
# )
router.register(
    "payment-status",
    PaymentStatusReadOnlyViewSet,
    "payment-status",
)
router.register(
    "user-type",
    UserTypeReadOnlyViewSet,
    "user-type",
)


urlpatterns = router.urls
