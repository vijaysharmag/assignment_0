from rest_framework import serializers
from .models import Product, Category

class ReadCategorySerailizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class ReadProductSerailizer(serializers.ModelSerializer):
    category = ReadCategorySerailizer()

    class Meta:
        model = Product
        fields = '__all__'


