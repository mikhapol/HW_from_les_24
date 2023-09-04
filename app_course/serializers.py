from rest_framework import serializers
from app_course.models import Course
from app_lesson.serializers import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели курса"""
    lessons_count = serializers.SerializerMethodField()  # Тип поля отвечающий за описание подсчёта количества уроков.
    lessons = LessonSerializer(many=True, source='lesson')  # Тип поля отвечающий за вывод уроков.

    def get_lessons_count(self, instance):
        """Метод отвечающий за подсчёт"""
        return instance.lesson.count()

    class Meta:
        model = Course
        fields = '__all__'
