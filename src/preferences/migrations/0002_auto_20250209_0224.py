# Generated by Django 5.1.6 on 2025-02-08 20:54

from django.db import migrations
from src.preferences.schemas import DTYPE


def create_default_preferences(apps, schema_editor):
    Preference = apps.get_model("preferences", "Preference")

    data = [
        {
            "key": "LANG",
            "dtype": DTYPE.STRING.value,
            "description": "Default language for the application",
        },
        {
            "key": "default_timezone",
            "dtype": DTYPE.STRING.value,
            "description": "Default timezone for the application",
        },
        {
            "key": "default_date_format",
            "dtype": DTYPE.STRING.value,
            "description": "Default date format for the application",
        },
        {
            "key": "default_time_format",
            "dtype": DTYPE.STRING.value,
            "description": "Default time format for the application",
        },
    ]
    for item in data:
        Preference.objects.create(**item)


class Migration(migrations.Migration):

    dependencies = [
        ("preferences", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_default_preferences),
    ]
