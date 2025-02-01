from django.db import models
from common.audit.models import HistoricalAuditModel
from users.models import User
from enums.enums import PaymentStatus
from courses.models import Course
from django.core.validators import MinValueValidator
from django.utils.timezone import now


class Order(HistoricalAuditModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    payment_status = models.IntegerField(choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    payment_image = models.ImageField(null=True, blank=True)
    payment_code = models.TextField(null=True, blank=True)


class OrderCourse(HistoricalAuditModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="courses")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="order_courses")
    include_videos = models.BooleanField(default=False)
    include_files = models.BooleanField(default=False)
    include_quizzes = models.BooleanField(default=False)
    price = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(0.01)])
    expires_at = models.DateTimeField()

    @property
    def is_expired(self):
        """Returns True if the expiration time has passed, False otherwise."""
        return self.expires_at < now()
