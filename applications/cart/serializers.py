from .models import Cart
from rest_framework import serializers


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'item', 'quantity', 'created_at', 'updated_at']