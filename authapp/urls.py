from django.contrib import admin
from django.urls import path,include
from authapp.views import index


urlpatterns = [
    path('',include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]
