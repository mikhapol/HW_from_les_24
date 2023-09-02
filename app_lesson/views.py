from rest_framework import generics
from app_lesson.models import Lesson
from app_lesson.serializers import LessonSerializer


class LessonCreateAPIView(generics.CreateAPIView):
    """View to create a lesson"""
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    """View to get a list of lessons"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """View to get a singe lesson by id"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """View to edit a lesson by id"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    """View to delete a lesson by id"""
    queryset = Lesson.objects.all()
