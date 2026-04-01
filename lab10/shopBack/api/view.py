from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import *


from .serializers import CategorySerializer, ProductSerializer
from .models import Product, Category




class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @action(['GET'], detail=True, url_path='products', url_name='products')
    def get_products_by_category(self, request, pk):
        query = Product.objects.filter(category_id=pk)
        serializer = ProductSerializer(query, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    

