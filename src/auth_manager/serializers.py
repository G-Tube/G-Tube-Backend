from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from src.user_manager import models as user_models

IN_CLAIM_PREFERENCES = ("default_language",)


class CustomObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user: user_models.User):
        token = super().get_token(user)

        for pref in IN_CLAIM_PREFERENCES:
            query = user_models.UserPreference.objects.filter(
                user=user, preference__key=pref
            )
            if query.exists():
                token[pref] = query.get(preference__key=pref).value

        return token
