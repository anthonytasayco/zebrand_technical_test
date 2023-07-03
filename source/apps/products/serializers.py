from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source="brand.name", read_only=True)

    class Meta:
        model = Product
        fields = [
            'slug', 'is_active', 'brand_name', 'sku', 'name', 'price', 'brand'
        ]
