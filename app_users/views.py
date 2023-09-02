from rest_framework.viewsets import ModelViewSet

from app_users.models import User
from app_users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """
    Набор представлений для пользовательской модели. Для создания необходимо ввести 'адрес электронной почты' и 'пароль'
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
