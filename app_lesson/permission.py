from rest_framework.permissions import BasePermission

from app_users.models import UserRoles


class IsOwner(BasePermission):
    """Права доступа для владельца."""
    message = "Вы не являетесь владельцем."

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsStaff(BasePermission):
    """Модератор может все кроме удаления и создания объектов."""
    message = "Вы не являетесь модератором."

    def has_permission(self, request, view):
        """
        Два варианта
        1 - Вариант без админки
        2 - Вариант с админкой - Active
        """
        # if request.user.is_staff:
        #     if request.method in ['DELETE', 'POST']:
        #         return False
        #     return True

        if request.user.role == UserRoles.MODERATOR:
            return True
        return False
