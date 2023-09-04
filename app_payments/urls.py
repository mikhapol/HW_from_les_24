from django.urls import path
from app_payments.views import PaymentListAPIView, PaymentCreateAPIView
from app_payments.apps import AppPaymentsConfig


app_name = AppPaymentsConfig.name

urlpatterns = [
    path('', PaymentListAPIView.as_view(), name='payments'),
    path('create/', PaymentCreateAPIView.as_view(), name='payments_create'),
]
