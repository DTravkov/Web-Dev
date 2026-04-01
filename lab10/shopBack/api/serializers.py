from rest_framework import serializers
from .models import Product, Category



class ProductSerializer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'is_active', 'category')
        read_only_fields = ['id']

    

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be positive")
        return value

    def validate_name(self, value:str):
        if not value or value.strip() == "":
            raise serializers.ValidationError("Product name can not be empty")
        if value.isdigit():
            raise serializers.ValidationError("Product name can not consist of numbers only")
        return value.strip()


class CategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = Category
        fields = ('id', 'name')
        read_only_fields = ['id']
    
    def validate_name(self, value:str):
        if not value or value.strip() == "":
            raise serializers.ValidationError("Category name can not be empty")
        if value.isdigit():
            raise serializers.ValidationError("Category name can not consist of numbers only")
        return value.strip()

    
