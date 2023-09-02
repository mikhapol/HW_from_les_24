from rest_framework.viewsets import ModelViewSet
from app_course.models import Course
from app_course.serializers import CourseSerializer


class CourseViewSet(ModelViewSet):
    """Viewset for Course model"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
