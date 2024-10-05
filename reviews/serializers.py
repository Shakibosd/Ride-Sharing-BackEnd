from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Review
        fields = '__all__'

class ReviewSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'