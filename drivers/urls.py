from django.urls import path
from .views import DriverListCreateAPIView, DriverDetailAPIView,accept_ride

urlpatterns = [
    path('drivers/', DriverListCreateAPIView.as_view(), name='driver-list-create'),
    path('drivers/<int:pk>/', DriverDetailAPIView.as_view(), name='driver-detail'),
    path('accept/<int:ride_id>/', accept_ride, name='accept_ride'),
]
