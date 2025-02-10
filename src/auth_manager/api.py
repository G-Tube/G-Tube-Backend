from django.http import response as djresponse
from jwcrypto import jwk
from rest_framework import exceptions, permissions, status, views
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt import exceptions as jwt_exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


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


class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]


class RefreshView(TokenRefreshView):
    permission_classes = [permissions.AllowAny]
