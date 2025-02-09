from django.db import models
from django.template.defaulttags import comment

from src.common.models import BaseModel


# Create your models here.
class Video(BaseModel):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to="videos/")
    thumbnail = models.ImageField(upload_to="thumbnails/", null=True, blank=True)
    description = models.TextField()
    is_public = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    owner = models.ForeignKey("user_manager.User", on_delete=models.CASCADE)

    likes = models.ManyToManyField(
        "user_manager.User",
        related_name="liked_videos",
        through="VideoLikes",
    )

    comments = models.ManyToManyField(
        "user_manager.User",
        related_name="commented_videos",
        through="VideoComments",
    )

    @property
    def like_count(self):
        return self.likes.count()

    @property
    def deleted(self):
        return self.deleted_at is not None

    @property
    def comment_count(self):
        return self.comments.count()


class VideoLikes(BaseModel):
    video = models.ForeignKey("Video", on_delete=models.CASCADE)
    user = models.ForeignKey("user_manager.User", on_delete=models.CASCADE)

    class Meta:  # type: ignore
        unique_together = ["video", "user"]


class VideoComments(BaseModel):
    video = models.ForeignKey("Video", on_delete=models.CASCADE)
    user = models.ForeignKey("user_manager.User", on_delete=models.CASCADE)
    comment = models.TextField()
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
