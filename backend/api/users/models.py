from django.db import models
from enums.enums import UserType
from common.audit.models import HistoricalAuditModel
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Univeristy(HistoricalAuditModel):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="univeristies/", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Univeristies"


class Specialization(HistoricalAuditModel):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="specializations/", null=True, blank=True)

    def __str__(self):
        return self.name


class City(HistoricalAuditModel):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="cities/", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"


class User(AbstractUser, HistoricalAuditModel):
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    univeristy = models.ForeignKey(Univeristy, on_delete=models.SET_NULL, null=True, blank=True, related_name="users")
    specialization = models.ForeignKey(
        Specialization, on_delete=models.SET_NULL, null=True, blank=True, related_name="users"
    )
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name="users")
    device_id = models.CharField(max_length=300, unique=True)
    full_name = models.CharField(max_length=300, default="")
    image = models.ImageField(upload_to="users/", null=True, blank=True)
    type = models.IntegerField(choices=UserType.choices, default=UserType.STUDENT)
    whatsapp = PhoneNumberField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.full_name


class Experience(HistoricalAuditModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="experiences")
    text = models.CharField(max_length=300)
