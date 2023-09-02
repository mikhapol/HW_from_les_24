from app_users.apps import AppUsersConfig
from rest_framework.routers import DefaultRouter

from app_users.views import UserViewSet

app_name = AppUsersConfig.name

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [

] + router.urls