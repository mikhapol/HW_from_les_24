from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from app_course.models import Course
from app_course.permission import IsOwner
from app_course.serializers import CourseSerializer
from app_lesson.permission import IsStaff


# Описание CRUD для моделей курса через ViewSets.
class CourseViewSet(ModelViewSet):
    """Набор представлений для модели курса"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        """Права доступа"""
        if self.action == 'retrieve':
            permission_classes = [IsOwner | IsStaff]
        elif self.action == 'create':
            permission_classes = [IsStaff]
        elif self.action == 'destroy':
            permission_classes = [IsOwner | IsStaff]
        elif self.action == 'update':
            permission_classes = [IsOwner | IsStaff]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
