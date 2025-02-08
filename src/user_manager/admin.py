from django.contrib import admin
from src.user_manager.models import User
from django.contrib.auth.admin import UserAdmin as _UserAdmin


# Register your models here.
@admin.register(User)
class UserAdmin(_UserAdmin):
    pass
