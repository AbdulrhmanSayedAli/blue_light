from rest_framework import routers
from .views import (
    OsTypeReadOnlyViewSet,
    GenderReadOnlyViewSet,
    NotificationObjectTypeReadOnlyViewSet,
    NotificationTemplateTypeReadOnlyViewSet,
)


router = routers.DefaultRouter()

router.register("os-types", OsTypeReadOnlyViewSet, "os-types")
router.register("gender", GenderReadOnlyViewSet, "gender")
router.register(
    "notification-object-type",
    NotificationObjectTypeReadOnlyViewSet,
    "notification-object-type",
)
router.register(
    "notification-template-type",
    NotificationTemplateTypeReadOnlyViewSet,
    "notification-template-type",
)


urlpatterns = router.urls
