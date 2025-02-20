# Generated by Django 5.1.6 on 2025-02-09 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UploadJob",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255)),
                ("raw_video", models.FileField(upload_to="raw_videos/")),
                (
                    "thumbnail",
                    models.ImageField(blank=True, null=True, upload_to="thumbnails/"),
                ),
                ("description", models.TextField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("draft", "DRAFT"),
                            ("submitted", "SUBMITTED"),
                            ("processing", "PROCESSING"),
                            ("completed", "COMPLETED"),
                        ],
                        default="draft",
                        max_length=255,
                    ),
                ),
                ("is_public", models.BooleanField(default=False)),
                (
                    "log_file",
                    models.FileField(blank=True, null=True, upload_to="logs/"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
