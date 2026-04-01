from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import *
from rest_framework.exceptions import APIException, NotFound


from ..serializers import ProductSerializer
from ..models import Product

def get_object(product_id: int):
    try:
        return Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise NotFound(detail=f"Product with id {product_id} is not found.", code=HTTP_404_NOT_FOUND)

def get_all():
    return Product.objects.all()


class ProductListAPIView(APIView):
       
    def post(self, request: Request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)
    
    def get(self, request: Request):
        serializer = ProductSerializer(get_all(), many=True)
        return Response(serializer.data, status=HTTP_200_OK)
        
class ProductDetailAPIView(APIView):
       
    def put(self, request: Request, product_id: int):
        serializer = ProductSerializer(get_object(product_id), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)
    
    def get(self, request: Request, product_id: int):
        serializer = ProductSerializer(get_object(product_id))
        return Response(serializer.data, status=HTTP_200_OK)
    
    def delete(self, request: Request, product_id: int):
        get_object(product_id).delete()
        return Response(status=HTTP_204_NO_CONTENT)