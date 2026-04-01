from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import *
from rest_framework.exceptions import APIException
from django.shortcuts import get_object_or_404

from ..serializers import ProductSerializer
from ..models import Product


class ProductListAPIView:
    def as_view():
        @api_view(['GET', 'POST'])
        def products_list(request: Request):
            if request.method == 'GET':
                serializer = ProductSerializer(Product.objects.all(), many=True)
                return Response(serializer.data, status=HTTP_200_OK)
            if request.method == 'POST':
                serializer = ProductSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=HTTP_201_CREATED)
            
        return products_list
    
class ProductDetailAPIView:
    def as_view():
        @api_view(['GET', 'PUT', 'DELETE'])
        def product_detail(request: Request, product_id: int):
            product_object = get_object_or_404(Product, pk=product_id)

            if request.method == 'GET':
                serializer = ProductSerializer(product_object)
                return Response(serializer.data, status=HTTP_200_OK)
            if request.method == 'PUT':
                serializer = ProductSerializer(product_object, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data, status=HTTP_200_OK)
            if request.method == 'DELETE':
                product_object.delete()
                return Response(status=HTTP_204_NO_CONTENT)
                    
        return product_detail

    

