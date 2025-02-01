from .base.views import EnumReadOnlyViewSet
from .enums import OsType, Gender, NotificationObjectType, NotificationTemplateType, PaymentStatus, UserType


class OsTypeReadOnlyViewSet(EnumReadOnlyViewSet):
    enum = OsType


class GenderReadOnlyViewSet(EnumReadOnlyViewSet):
    enum = Gender


class NotificationObjectTypeReadOnlyViewSet(EnumReadOnlyViewSet):
    enum = NotificationObjectType


class NotificationTemplateTypeReadOnlyViewSet(EnumReadOnlyViewSet):
    enum = NotificationTemplateType


class PaymentStatusReadOnlyViewSet(EnumReadOnlyViewSet):
    enum = PaymentStatus


class UserTypeReadOnlyViewSet(EnumReadOnlyViewSet):
    enum = UserType
