
from django.contrib import admin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin

class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("username", "first_name", "last_name")}),  
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"), 
            },
        ),
    )
    list_display = ("email", "username", "first_name", "last_name", "is_staff")  
    search_fields = ("email", "username", "first_name", "last_name") 
    ordering = ("email",)
    readonly_fields = ['date_joined', 'last_login']

class ProfilerAdmin(admin.ModelAdmin):
    list_display = ['user','phone','birthday','city']

admin.site.register(CustomUser,UserAdmin )