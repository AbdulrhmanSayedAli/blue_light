from django.db import models
from enums.enums import UserType
from common.audit.models import HistoricalAuditModel
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Univeristy(HistoricalAuditModel):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Univeristies"


class Specialization(HistoricalAuditModel):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)


class City(HistoricalAuditModel):
    name = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Cities"


class User(AbstractUser, HistoricalAuditModel):
    phone_number = PhoneNumberField(null=True, blank=True)
    full_name = models.CharField(max_length=300, null=True, blank=True, default="")
    univeristy = models.ForeignKey(Univeristy, on_delete=models.SET_NULL, null=True, blank=True, related_name="users")
    specialization = models.ForeignKey(
        Specialization, on_delete=models.SET_NULL, null=True, blank=True, related_name="users"
    )
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name="users")
    device_id = models.CharField(max_length=300)
    image = models.ImageField(null=True, blank=True)
    type = models.IntegerField(choices=UserType.choices, default=UserType.STUDENT)
    whatsapp = PhoneNumberField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)


class Experience(HistoricalAuditModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="experiences")
    text = models.CharField(max_length=300)
