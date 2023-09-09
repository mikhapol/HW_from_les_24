from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Права доступа для суперюзера."""
    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class IsStaff(BasePermission):
    def has_permission(self, request, view):
        """Модератор может все кроме удаления и создания объектов."""
        if request.user.is_staff:
            if request.method in ['DELETE', 'POST']:
                return False
            return True
