from django.db import models
from common.audit.models import HistoricalAuditModel
from users.models import User
from enums.enums import PaymentStatus
from courses.models import Course


class Order(HistoricalAuditModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    payment_status = models.IntegerField(choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    payment_image = models.ImageField(null=True, blank=True)
    payment_code = models.TextField(null=True, blank=True)


class OrderCourse(HistoricalAuditModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="courses")
