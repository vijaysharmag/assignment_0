from rest_framework import viewsets
from django.core.cache import cache
from .models import Product
from product.utils import ReadNestedViewMixin
from .serializers import ProductSerializer, ReadProductSerailizer

class ProductViewSet(ReadNestedViewMixin, viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    read_serializer_class = ReadProductSerailizer

    def get_queryset(self):
        queryset = cache.get('product')

        if queryset is None:
            queryset = super().get_queryset()
            cache.set('product', queryset, timeout=20)

        return queryset
    

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        cache.clear()
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.clear()
        return response

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.clear()
        return response
