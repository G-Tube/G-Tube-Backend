from django.urls import path

from src.auth_manager import api as auth_api

urlpatterns = [
    path("login/", auth_api.LoginView.as_view(), name="login"),
    path("refresh/", auth_api.RefreshView.as_view(), name="refres-token"),
]

absolute_urlpatterns = [
    path(".well-known/jwks.json", auth_api.JwkView.as_view(), name="jwks"),
]
