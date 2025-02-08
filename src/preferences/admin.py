from django.contrib import admin
from src.preferences.models import Preference


@admin.register(Preference)
class PreferenceAdmin(admin.ModelAdmin):
    list_display = ("key", "dtype", "description")
    search_fields = ("key", "description")
    list_filter = ("dtype",)
    ordering = ("key",)
