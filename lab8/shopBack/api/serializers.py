from rest_framework import serializers
from .models import Product, ProductCategory



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'is_active', 'category')
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be positive")
        return value
    


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = ProductCategory
        fields = ('name')
    def validate_name(self, value:str):
        if not value or value.strip() == "":
            raise serializers.ValidationError("Category name can not be empty")
        if value.isdigit():
            raise serializers.ValidationError("Category name can not consist of numbers only")
        return value.strip()

    
