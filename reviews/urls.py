from django.urls import path
from .views import ReviewListCreateAPIView, ReviewDetailAPIView, ReviewListCreateAPIViewGet

urlpatterns = [
    path('review_list_create/<int:driverId>/', ReviewListCreateAPIView.as_view(), name='review-list-create'),#ata post er api
    path('reviews_detail/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail'),#eta get,put,delete er api
    path('reviews_detail_get/<int:driverId>/', ReviewListCreateAPIViewGet.as_view(), name='review-detail-get'),#eta get er api
]