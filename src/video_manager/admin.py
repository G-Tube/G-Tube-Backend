from django.contrib import admin

from src.video_manager.models import Video, VideoComments, VideoLikes


# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "thumbnail",
        "description",
        "owner",
        "is_public",
        "deleted",
        "like_count",
        "comment_count",
    ]
    search_fields = ["title", "description", "owner__username"]
    list_filter = ["is_public", "deleted_at", "owner__username"]


@admin.register(VideoComments)
class VideoCommentsAdmin(admin.ModelAdmin):
    list_display = [
        "video",
        "user",
        "comment",
        "parent",
    ]
    search_fields = ["video__title", "video__description", "user__username", "comment"]
    list_filter = ["video", "user", "parent"]
