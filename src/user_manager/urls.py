from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from src.user_manager import api as user_api


def inject_urls(router):
    router.register(r"users", user_api.UserViewSet, basename="users")


urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("refresh/", TokenRefreshView.as_view(), name="refres-token"),
]

absolute_urlpatterns = [
    path(".well-known/jwks.json", user_api.JwkView.as_view(), name="jwks"),
]
