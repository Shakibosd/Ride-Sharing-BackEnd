from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/',views.RegisterAPIView.as_view(), name='register'),
    path('login/',views.LoginAPIView.as_view(), name='login'),
    path('logout/',views.LogoutAPIView.as_view(), name='logout'),
    path('active/<uid64>/<token>/',views.activate, name='active')
]

