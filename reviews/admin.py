from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'driver', 'rating', 'comment', 'created_at']

admin.site.register(Review, ReviewAdmin)
