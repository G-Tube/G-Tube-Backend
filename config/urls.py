"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions, routers

from src.auth_manager import urls as auth_urls
from src.preferences import urls as pref_urls
from src.user_manager import urls as user_urls

router = routers.DefaultRouter()
router.APISchemaView.public = True
router.APISchemaView.permission_classes = [permissions.AllowAny]
router.APIRootView.permission_classes = [permissions.AllowAny]

pref_urls.inject_urls(router)
user_urls.inject_urls(router)

absolute_urlpatterns = []
absolute_urlpatterns += auth_urls.absolute_urlpatterns

urlpatterns = (
    [
        path("", include(absolute_urlpatterns)),
        path("admin", admin.site.urls),
        path("api/", include(router.urls)),
        path("api/auth/", include(auth_urls.urlpatterns)),
    ]
    + static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + debug_toolbar_urls()
    if settings.DEBUG
    else []
)
