from django.urls import path
from .views import PaymentListCreateAPIView, PaymentDetailAPIView, PaymentListCreateAPIViewGet

urlpatterns = [
    path('payments/', PaymentListCreateAPIView.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentDetailAPIView.as_view(), name='payment-detail'),
    path('payments_get/', PaymentListCreateAPIViewGet.as_view(), name='payment-detail-get'),
]
