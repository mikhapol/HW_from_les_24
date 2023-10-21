from rest_framework import serializers

from app_payments.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели платежа"""
    class Meta:
        model = Payment
        fields = '__all__'
