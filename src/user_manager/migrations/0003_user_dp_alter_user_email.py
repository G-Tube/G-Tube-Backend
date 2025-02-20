# Generated by Django 5.1.6 on 2025-02-09 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_manager", "0002_auto_20250209_0225"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="dp",
            field=models.ImageField(
                default="../static/default-dp.jpg", upload_to="profile_pics"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                max_length=254, unique=True, verbose_name="email address"
            ),
        ),
    ]
