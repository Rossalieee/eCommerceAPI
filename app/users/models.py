from django.db import models
from django.contrib.auth.models import AbstractUser
from .enums import UserRole


class MyUser(AbstractUser):
    role = models.CharField(choices=UserRole.choices, default=UserRole.CUSTOMER, max_length=20)
