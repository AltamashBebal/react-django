from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.
from rest_framework import serializers

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




# class userProfileSerializer(serializers.ModelSerializer):
#     user=CurrentUserSerializer(read_only=True)
#     class Meta:
#         model=User
#         fields='__all__'