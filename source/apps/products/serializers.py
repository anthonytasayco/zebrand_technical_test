from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'is_active', 'sku', 'name', 'price', 'brand'
        ]
