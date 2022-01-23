import re
from django.shortcuts import render

# Create your views here.
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from .models import User
from django.http import JsonResponse
from rest_framework import serializers

@api_view(['GET'])
def index(request):
    date=datetime.now().strftime("%Y-%m-%d")
    message='server is running'
    return Response(data=message,status=status.HTTP_200_OK)


# @api_view(['DELETE'])
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def delete(request, user_name):
        user = User.objects.filter(username=user_name)
        print(user)
        if user:
            user.delete()
            return HttpResponse(status=200)

        return HttpResponse(status=404)        #     return Response(request,{"status":"ok"}, status=status.HTTP_200_OK)
        # return Response(request,serializers.errors, status=status.HTTP_400_BAD_REQUEST)    