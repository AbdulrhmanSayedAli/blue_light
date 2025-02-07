from django.db import models
from common.audit.models import HistoricalAuditModel
from users.models import User


class Rate(HistoricalAuditModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="rate")
    performance_of_the_application = models.DecimalField(max_digits=3, decimal_places=2)
    clarity_and_variety_of_materials = models.DecimalField(max_digits=3, decimal_places=2)
    response_and_interaction_of_the_trainer = models.DecimalField(max_digits=3, decimal_places=2)
    courses_helped_you = models.DecimalField(max_digits=3, decimal_places=2)
    notes = models.TextField(null=True, blank=True)
