from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'gender', 'birthday', 'city', 'country', 'postal_code', 'last_updated')
    list_filter = ('gender', 'city', 'country')
    # search_fields = ('user__email','phone')
    list_per_page = 20

admin.site.register(Profile, ProfileAdmin)

