from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

roles = (
    ("admin", "Admin"),
    ("customer", "Customer"),
    ("delivery Boy", "Delivery Boy"),

)


class User(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=roles,
    )
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    group = models.CharField(max_length=20)
    REQUIRED_FIELDS = ['phone', 'first_name', 'last_name', 'role']
