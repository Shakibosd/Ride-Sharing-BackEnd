from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls')),
    path('rides/',include('rides.urls')),
    path('drivers/',include('drivers.urls')),
    path('payments/',include('payments.urls')),
    path('reviews/',include('reviews.urls')),
    path('profiles/',include('profiles.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
