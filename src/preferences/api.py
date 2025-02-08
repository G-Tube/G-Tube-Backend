from rest_framework import permissions, serializers, viewsets
from rest_framework.decorators import action
from src.preferences.models import Preference


class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:  # type: ignore
        model = Preference
        fields = "__all__"


class PreferenceViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PreferenceSerializer
    queryset = Preference.objects.all()
    permission_classes = [permissions.AllowAny]
