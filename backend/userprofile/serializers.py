from .models import Profile
from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer


class CustomLoginSerializer(LoginSerializer):
    username = None
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        

