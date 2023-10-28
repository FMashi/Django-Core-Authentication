from . models import CustomUser
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.backends import ModelBackend
from dj_rest_auth.serializers import LoginSerializer

class CustomLoginSerializer(LoginSerializer):
    username = None

        

