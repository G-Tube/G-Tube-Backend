from django.urls import include, path
from rest_framework.routers import DefaultRouter
from src.preferences.api import PreferenceViewSet


def inject_urls(router: DefaultRouter):
    router.register("preference", PreferenceViewSet, basename="preference")
