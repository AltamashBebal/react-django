from django.contrib import admin
from .models import CustomerWiseProduct,Product
# Register your models here.
admin.site.register(Product)
admin.site.register(CustomerWiseProduct)