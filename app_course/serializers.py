from rest_framework import serializers
from app_course.models import Course, Subscription
from app_lesson.models import Lesson
from app_lesson.serializers import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели курса"""
    lessons_count = serializers.SerializerMethodField()  # Тип поля отвечающий за описание подсчёта количества уроков.
    lessons = LessonSerializer(many=True, source='lesson', read_only=True)  # Тип поля отвечающий за вывод уроков.
    is_subscribed = serializers.SerializerMethodField()  # Проверка подписки

    def get_lessons_count(self, course):
        """Метод для получения количества уроков в курсе"""

        return Lesson.objects.filter(course=course).count()

    def get_lessons(self, course):
        """Метод для получения списка всех уроков в курсе"""

        return [lesson.title for lesson in course.lesson_set.all()]

    def get_is_subscribed(self, course):
        """Метод для проверки подписки к курсу"""

        return Subscription.objects.filter(course=course, user=self.context['request'].user).exists()

    class Meta:
        model = Course
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор для модели подписки"""

    class Meta:
        model = Subscription
        fields = '__all__'
