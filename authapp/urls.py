from django.contrib import admin
from django.urls import path,include
from authapp.views import index
from rest_framework import serializers
import views

urlpatterns = [
    path('',include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('user/delete/<str:user_name>',views.delete)

]
