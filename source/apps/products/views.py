from .models import Product, Category
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer, CategorySerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from .signals import viewed_product


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all().select_related('brand')
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        product = get_object_or_404(Product, slug=slug)
        serializer = ProductSerializer(product)
        viewed_product.send(sender=Product, product_slug=slug, user=request.user)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'id'

    def retrieve(self, request, id=None):
        category = get_object_or_404(Category, id=id)
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(
            products, many=True)
        return Response(serializer.data)
