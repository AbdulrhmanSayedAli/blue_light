from common.audit.models import HistoricalAuditModel
from django.db import models
from users.models import User
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.db.models import Sum
from datetime import timedelta


class Course(HistoricalAuditModel):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to="courses/")
    description_video = models.URLField(null=True, blank=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    duration_in_days = models.IntegerField()

    def __str__(self):
        return self.name

    @property
    def videos_count(self):
        return len(self.videos.all())

    @property
    def files_count(self):
        return len(self.files.all())

    @property
    def quizzes_count(self):
        return len(self.quizzes.all())

    @property
    def videos_duration(self):
        total_duration = self.videos.aggregate(total_duration=Sum("duration"))["total_duration"]
        return total_duration or timedelta()

    @property
    def videos_duration_human_readable(self):
        total_duration = self.videos_duration

        if not total_duration:
            return "0h 0m 0s"

        # Convert to seconds
        total_seconds = int(total_duration.total_seconds())

        # Calculate hours, minutes, and seconds
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        # Create human-readable string based on values
        parts = []
        if hours > 0:
            parts.append(f"{hours}h")
        if minutes > 0 or hours > 0:  # Always show minutes if hours exist
            parts.append(f"{minutes}m")
        parts.append(f"{seconds}s")

        return " ".join(parts)

    @property
    def videos_price(self) -> float:
        return sum(video.price for video in self.videos.all())

    @property
    def files_price(self) -> float:
        return sum(file.price for file in self.files.all())

    @property
    def quizzes_price(self) -> float:
        return sum(quizz.price for quizz in self.quizzes.all())

    @property
    def price(self) -> float:
        return self.videos_price + self.files_price + self.quizzes_price


class CourseGroup(HistoricalAuditModel):
    name = models.CharField(max_length=300)
    image = models.ImageField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="groups")

    def __str__(self):
        return self.name


class Video(HistoricalAuditModel):
    name = models.CharField(max_length=300)
    duration = models.DurationField(null=True, blank=True)
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
    info = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(0.01)])
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class File(HistoricalAuditModel):
    name = models.CharField(max_length=300)
    pages_count = models.IntegerField(default=0, null=True, blank=True, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to="courses/files/", null=True, blank=True)
    file = models.FileField(upload_to="courses/files/", null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="files")
    info = models.TextField(null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(0.01)])
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Quiz(HistoricalAuditModel):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to="courses/quizzes/", null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="quizzes")
    is_public = models.BooleanField(default=False)
    info = models.TextField(null=True, blank=True)
    info_title = models.CharField(max_length=300, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(0.01)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Quizzes"


class Question(HistoricalAuditModel):
    text = models.CharField(max_length=400)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")

    def __str__(self):
        return self.text


class Answer(HistoricalAuditModel):
    text = models.CharField(max_length=400)
    is_true_answer = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")

    def __str__(self):
        return self.text
