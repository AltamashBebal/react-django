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
from .serializers import CurrentUserSerializer

@api_view(['GET'])
def index(request):
    date=datetime.now().strftime("%Y-%m-%d")
    message='server is running' 
    return Response(data=message,status=status.HTTP_200_OK)


from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def delete(request, user_name):
        user = User.objects.filter(username=user_name)
        if user:
            user.delete()
            return HttpResponse(status=200)

        return HttpResponse(status=404)        #     return Response(request,{"status":"ok"}, status=status.HTTP_200_OK)
  
from rest_framework.renderers import JSONRenderer

# @api_view(['GET'])
@csrf_exempt
def getUsers(request):
    user = User.objects.all()
    serializer = CurrentUserSerializer(user,many=True)
    data = serializer.data
    print(data)
    json = JSONRenderer().render(serializer.data)
    json
    # return data["json"]
    return HttpResponse(json,status=status.HTTP_200_OK)

@csrf_exempt
def getUser(request,username):
    user = User.objects.filter(username=username)
    if user:
        serializer = CurrentUserSerializer(user,many=True)
        data = serializer.data
        # print(data)
        json = JSONRenderer().render(serializer.data)
        # json
        # return data["json"]
        return HttpResponse(json,status=status.HTTP_200_OK)    
    return HttpResponse(status=status.HTTP_404_NOT_FOUND)    