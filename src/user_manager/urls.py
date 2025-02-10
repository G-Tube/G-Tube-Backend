from src.user_manager import api as user_api


def inject_urls(router):
    router.register(r"users", user_api.UserViewSet, basename="users")
