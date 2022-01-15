from djoser.serializers import UserSerializer,UserCreateSerializer
from rest_framework import serializers
from .models import *


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields =('id','email','username','password','first_name', 'last_name','group','address','role')
