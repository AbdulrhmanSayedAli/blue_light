from common.audit.models import HistoricalAuditModel
from django.db import models
from users.models import User
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _


class Course(HistoricalAuditModel):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to="courses/")
    description_video = models.URLField(null=True, blank=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    duration_in_days = models.IntegerField()

    @property
    def price(self) -> float:
        videos_price = sum(video.price for video in self.videos.all())
        files_price = sum(file.price for file in self.files.all())
        return videos_price + files_price


class CourseGroup(HistoricalAuditModel):
    name = models.CharField(max_length=300)
    image = models.ImageField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="groups")


class Video(HistoricalAuditModel):
    name = models.CharField(max_length=300)
    duration = models.DurationField()
    image = models.ImageField(upload_to="courses/videos/", null=True, blank=True)
    url = models.URLField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="videos")
    group = models.ForeignKey(
        CourseGroup,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="videos",
    )
    info = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(0.01)])
    is_public = models.BooleanField(default=False)


class File(HistoricalAuditModel):
    name = models.CharField(max_length=300)
    pages_count = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to="courses/files/", null=True, blank=True)
    file = models.FileField(upload_to="courses/files/", null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="files")
    info = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(0.01)])
    is_public = models.BooleanField(default=False)
