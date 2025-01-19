from django.db import models
from common.audit.models import HistoricalAuditModel
from courses.models import Course


class AD(HistoricalAuditModel):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="ads/")

    def __str__(self):
        return self.name


class Section(HistoricalAuditModel):
    name = models.CharField(max_length=250)
    courses = models.ManyToManyField(Course, related_name="+")

    def __str__(self):
        return self.name
