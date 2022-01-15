import re
from django.shortcuts import render

# Create your views here.
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

@api_view(['GET'])
def index(request):
    date=datetime.now().strftime("%Y-%m-%d")
    message='server is running'
    return Response(data=message,status=status.HTTP_200_OK)