from rest_framework import serializers

from app_users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Пользователь"""
    class Meta:
        model = User
        fields = ('email', 'password', 'phone', 'city', 'avatar')
