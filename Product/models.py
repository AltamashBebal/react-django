from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# from .models import Product

class Product(models.Model):
    p_id = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=255)

    def __str__(self):
        return self.pname


class CustomerWiseProduct(models.Model):
    pc_id = models.AutoField(primary_key=True)
    c_name=models.CharField(max_length=255)
    pname=models.ForeignKey(Product,on_delete=models.CASCADE)
    pprice=models.CharField(max_length=255)

    def __str__(self):
        return self.c_name