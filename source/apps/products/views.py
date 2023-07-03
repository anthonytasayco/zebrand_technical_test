from .models import Product
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser


class ProductViewSet(viewsets.ViewSet):
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

    def retrieve(self, request, pk=None):
        product = get_object_or_404(queryset, slug=slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
