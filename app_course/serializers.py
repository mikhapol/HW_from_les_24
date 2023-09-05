from rest_framework import serializers
from app_course.models import Course
from app_lesson.serializers import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели курса"""
    lessons_count = serializers.SerializerMethodField()  # Тип поля отвечающий за описание подсчёта количества уроков.
    # lessons = LessonSerializer(many=True, source='lesson')  # Тип поля отвечающий за вывод уроков.
    lessons = serializers.SerializerMethodField(
        read_only=True)  # добавляем поле уроков и делаем метод для получения уроков

    def get_lessons_count(self, instance):
        """Метод отвечающий за подсчёт"""
        return instance.lesson.count()

    def get_lessons(self, obj):
        """Добавление уроков для курса"""
        lesson_list = []
        if obj.lesson.all():
            for i in obj.lesson.all().values_list():  # проходимся циклом по всем связанным урокам
                lesson_list.append  # добавляем в список урок
                return lesson_list
        return None

    class Meta:
        model = Course
        fields = '__all__'
