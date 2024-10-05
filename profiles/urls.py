from django.urls import path, include
from profiles.views import userProfileDetails
from rest_framework.routers import DefaultRouter
from .views import ChangePasswordViewSet

router = DefaultRouter()
router.register(r'pass_cng', ChangePasswordViewSet, basename='pass_cng')

urlpatterns = [
    path('', include(router.urls)),
    path('user_detail/<int:id>/', userProfileDetails.as_view(), name='user-detail'),
]