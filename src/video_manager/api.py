from rest_framework import mixins, serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from video_manager.models import Video, VideoComments, VideoLikes


class VideoViewSet(
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    class VideoSerializer(serializers.ModelSerializer):
        class Meta:  # type: ignore
            model = Video
            fields = (
                "id",
                "title",
                "video",
                "thumbnail",
                "description",
                "is_public",
                "owner",
            )

    class CommentOutSerializer(serializers.ModelSerializer):
        class Meta:  # type: ignore
            model = VideoComments
            fields = ("id", "user", "comment", "parent")

    queryset = Video.objects.filter(deleted_at=None)
    serializer_class = VideoSerializer

    @action(detail=True, methods=["GET"], url_path="comments")
    def comments(self, request, pk):
        class CommentInSerializer(serializers.Serializer):
            parent_id = serializers.UUIDField(required=False)

        serializer = CommentInSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        parent = serializer.validated_data.get("parent_id")
        if parent:
            comments = VideoComments.objects.filter(video__pk=pk, parent=parent)
        else:
            comments = VideoComments.objects.filter(video__pk=pk)
        return self.get_serializer(comments, many=True).data

    @action(detail=True, methods=["GET"], url_path="like_count")
    def like_count(self, request, pk):
        video = self.get_object()
        return Response({"like_count": video.like_count})
