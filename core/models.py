from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.base_models import BaseModel, ID


class User(AbstractUser, BaseModel, ID):
    username = models.CharField(
        max_length=11,
        unique=True,
        verbose_name="نام کاربری",
    )

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"


class Patient(BaseModel, ID):
    user = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        related_name='patients',
        verbose_name="کاربر",
    )

    full_name = models.CharField(
        max_length=120,
        verbose_name="نام کامل",
    )

    age = models.PositiveIntegerField(
        verbose_name="سن",
    )

    class Meta:
        verbose_name = "بیمار"
        verbose_name_plural = "بیماران"
