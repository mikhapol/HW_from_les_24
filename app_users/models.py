from django.contrib.auth.models import AbstractUser
from django.db import models

from app_users.managers import UserManager

NULLABLE = {'blank': True, 'null': True}
NOT_NULLABLE = {'blank': False, 'null': False}


class User(AbstractUser):
    """Поля для модели обычного пользователя, но авторизация через email"""
    objects = UserManager()
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=35, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)

    verification_code = models.CharField(verbose_name='код верификации', max_length=255, **NULLABLE)
    is_verified = models.BooleanField( verbose_name='значение верификации', default=False, **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        db_table = 'users'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
