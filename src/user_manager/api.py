from django.db.models import Q
from django.http import response as djresponse
from jwcrypto import jwk
from rest_framework import exceptions, mixins, permissions, serializers, views, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework_simplejwt.settings import api_settings

from src.user_manager import models as user_manager_models


class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    class UserOutSerializer(serializers.ModelSerializer):
        class Meta:  # type: ignore
            model = user_manager_models.User
            fields = ("email", "username", "first_name", "last_name", "dp", "cover")

    class UserPreferenceOutSerializer(serializers.ModelSerializer):
        class Meta:  # type: ignore
            model = user_manager_models.UserPreference
            fields = ("preference__key", "preference_dtype", "value")
            read_only_fields = ("preference__key", "preference_dtype")

    serializer_class = UserOutSerializer
    lookup_field = "username"

    def list(self, request):
        class SearchUsersSerializer(serializers.Serializer):
            query = serializers.CharField(required=True, min_length=4)

        data = request.query_params
        serializer = SearchUsersSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        query = serializer.validated_data.get("query")

        users = user_manager_models.User.objects.filter(
            Q(email__icontains=query)
            | Q(username__icontains=query)
            | Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
        )[:10]
        return Response(self.UserOutSerializer(users, many=True).data)

    def get_queryset(self):
        user: user_manager_models.User = self.request.user  # type: ignore
        return user_manager_models.User.objects.filter(id=user.id)

    @action(detail=True, methods=["GET"], url_path="preferences")
    def preferences(self, request, username=None):
        user = get_object_or_404(user_manager_models.User, username=username)
        preferences = user.preferences.all()
        return Response(self.UserPreferenceOutSerializer(preferences, many=True).data)


class JwkView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):

        if not api_settings.JWK_URL:
            raise exceptions.NotFound()

        signing_key = api_settings.SIGNING_KEY

        if not signing_key:
            return

        key: jwk.JWK = jwk.JWK.from_pem(signing_key.encode("utf-8"))
        return djresponse.JsonResponse({"keys": [key.export_public(as_dict=True)]})
