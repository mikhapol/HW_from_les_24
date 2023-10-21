from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from app_payments.models import Payment
from app_payments.serializers import PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    """Класс для просмотра плажежей с возможностью сортировки и фильтрации"""
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # Бэкенд для обработки фильтра с сортировкой
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')  # Набор полей для фильтрации
    ordering_fields = ('date',)


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
