from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.base_models import BaseModel, ID


class User(AbstractUser, BaseModel, ID):
    username = models.CharField(max_length=11, unique=True)


class Patient(BaseModel, ID):
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name='patients')
    full_name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
