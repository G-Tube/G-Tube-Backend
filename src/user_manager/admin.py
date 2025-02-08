from django.contrib import admin
from src.user_manager.models import User, UserPreference
from django.contrib.auth.admin import UserAdmin as _UserAdmin


# Register your models here.
@admin.register(User)
class UserAdmin(_UserAdmin):
    list_display = ("email", "username", "first_name", "last_name", "is_staff")


@admin.register(UserPreference)
class UserPreferenceAdmin(admin.ModelAdmin):
    list_display = ("user", "preference__key", "value")
    list_filter = ("user",)
    ordering = ("user",)
