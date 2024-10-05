from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class PaymentSerializerGet(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    driver = serializers.SerializerMethodField() 
    class Meta:
        model = Payment
        fields = '__all__'

    def get_driver(self, obj):
            return obj.driver.name if obj.driver else 'N/A'        