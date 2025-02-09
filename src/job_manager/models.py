from django.db import models

from src.common.models import BaseModel
from src.job_manager.schemas import JobStatus


# Create your models here.
class UploadJob(BaseModel):
    title = models.CharField(max_length=255)
    raw_video = models.FileField(upload_to="raw_videos/")
    thumbnail = models.ImageField(upload_to="thumbnails/", null=True, blank=True)
    description = models.TextField()
    status = models.CharField(
        max_length=255, choices=JobStatus.choices(), default=JobStatus.DRAFT.value
    )
    is_public = models.BooleanField(default=False)
    log_file = models.FileField(upload_to="logs/", null=True, blank=True)
