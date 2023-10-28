from django.urls import path
from .views import getProfile,updateProfile



urlpatterns = [
    path('', getProfile, name='profile'),
    path('update/', updateProfile, name='update-profile'),
    
]
