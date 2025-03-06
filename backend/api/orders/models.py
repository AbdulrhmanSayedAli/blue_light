from django.db import models
from common.audit.models import HistoricalAuditModel
from users.models import User
from enums.enums import PaymentStatus
from courses.models import Course
from django.core.validators import MinValueValidator
from django.utils.timezone import now
import random
import string
from common.model_fields.decimal import PercentageField


class Order(HistoricalAuditModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    payment_status = models.IntegerField(choices=PaymentStatus.choices, default=PaymentStatus.PENDING)
    payment_image = models.ImageField(null=True, blank=True)
    payment_code = models.TextField(null=True, blank=True)
    coupon_code = models.CharField(max_length=50, null=True, blank=True)
    coupon_percentage = PercentageField(null=True, blank=True)

    @property
    def price(self) -> float:
        return sum(course.price for course in self.courses.all())

    def price_before_coupon(self) -> float:
        if not self.coupon_percentage:
            return self.price
        return (100 / (100 - self.coupon_percentage)) * self.price


class OrderCourse(HistoricalAuditModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_courses")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="order_courses")
    include_videos = models.BooleanField(default=False)
    include_files = models.BooleanField(default=False)
    include_quizzes = models.BooleanField(default=False)
    price = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(0.01)])
    expires_at = models.DateTimeField()

    def price_before_coupon(self) -> float:
        if not self.order.coupon_percentage:
            return self.price
        return (100 / (100 - self.order.coupon_percentage)) * self.price

    @property
    def is_expired(self):
        """Returns True if the expiration time has passed, False otherwise."""
        return self.expires_at < now()


def generate_coupon_code(length=10) -> str:
    characters = string.ascii_uppercase + string.digits  # A-Z and 0-9
    return "".join(random.choices(characters, k=length))


class Coupon(HistoricalAuditModel):
    code = models.CharField(max_length=50, default=generate_coupon_code)
    percentage = PercentageField()
    number_of_uses = models.IntegerField(default=1, validators=[MinValueValidator(0)])
