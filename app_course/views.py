from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from app_course.models import Course, Subscription
from app_course.permission import IsOwner
from app_course.serializers import CourseSerializer, SubscriptionSerializer
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


class SubscriptionCreateAPIView(generics.CreateAPIView):
    """Класс-представление для подписки курс на основе Generics"""

    serializer_class = SubscriptionSerializer  # класс-сериализатор

    def perform_create(self, serializer, **kwargs):
        """Переопределение метода perform_create для добавления пользователя"""
        new_subscription = serializer.save()  # создаем новую подписку

        new_subscription.user = self.request.user  # добавляем авторизованного пользователя
        new_subscription.course = Course.objects.get(id=self.kwargs['pk'])  # добавляем курс
        new_subscription.save()  # сохраняем новую подписку


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    """Удаление подписки на курс на основе Generics"""

    queryset = Course.objects.all()  # список уроков

    def perform_destroy(self, instance, **kwargs):
        """Переопределение метода perform_destroy для удаления подписки на курс"""

        user = self.request.user
        # получаем подписку
        subscription = Subscription.objects.get(course_id=self.kwargs['pk'], user=user)

        subscription.delete()  # удаляем подписку
