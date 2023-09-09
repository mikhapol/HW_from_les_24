from rest_framework import generics

from app_course.permission import IsOwner, IsStaff
from app_lesson.models import Lesson
from app_lesson.serializers import LessonSerializer


# Описание CRUD для моделей урока через Generic-классы.
class LessonCreateAPIView(generics.CreateAPIView):
    """View для создания урока"""
    serializer_class = LessonSerializer
    permission_classes = [IsOwner | IsStaff]


class LessonListAPIView(generics.ListAPIView):
    """View чтобы получить список уроков"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """View чтобы получить один урок по идентификатору"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsStaff]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """View чтобы отредактировать урок по идентификатору"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsStaff]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """View чтобы удалить урок по идентификатору"""
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner | IsStaff]
