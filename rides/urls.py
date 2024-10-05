from django.urls import path
from .views import RideListCreateAPIView,ContactFormView,IsAdminView, UserListView

urlpatterns = [
    path('rides/', RideListCreateAPIView.as_view(), name='ride-list-create'),
    path('contact/', ContactFormView.as_view(), name='contact-form'),
    path('is_admin/', IsAdminView.as_view(), name='is_admin'),
    path('user_list/', UserListView.as_view(), name='user_list'), 
]
