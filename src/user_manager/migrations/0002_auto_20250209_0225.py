# Generated by Django 5.1.6 on 2025-02-08 20:55

from django.db import migrations


def create_default_superuser(apps, schema_editor):
    User = apps.get_model("user_manager", "User")
    User.objects.create_superuser(
        username="admin", password="admin", email="admin@admin.com"
    )


class Migration(migrations.Migration):

    dependencies = [
        ("user_manager", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_default_superuser),
    ]
