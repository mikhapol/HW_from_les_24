from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app_lesson.models import Lesson
from app_lesson.permission import IsOwnerOrStaff
from app_lesson.serializers import LessonSerializer


# Описание CRUD для моделей урока через Generic-классы.
class LessonCreateAPIView(generics.CreateAPIView):
    """View для создания урока"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]


class LessonListAPIView(generics.ListAPIView):
    """View чтобы получить список уроков"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated | IsOwnerOrStaff]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """View чтобы получить один урок по идентификатору"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """View чтобы отредактировать урок по идентификатору"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated | IsOwnerOrStaff]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """View чтобы удалить урок по идентификатору"""
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
