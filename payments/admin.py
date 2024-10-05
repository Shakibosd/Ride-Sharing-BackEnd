from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'driver', 'amount', 'timestamp']

admin.site.register(Payment, PaymentAdmin)
    