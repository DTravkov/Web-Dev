from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import *

from .serializers import ProductCategorySerializer, ProductSerializer
from .models import Product, ProductCategory




class BaseView(APIView):
    model = None
    serializer_class = None

    def fetch_data(self,id):
        entry = None
        try:
            entry = self.model.objects.get(pk=id)
        except self.model.DoesNotExist:
            entry = None
        
        return entry
    

class BaseManyView(BaseView):
    def get(self, request):
        entry_list = self.model.objects.all()
        serializer = self.serializer_class(entry_list, many=True)

        return Response(serializer.data,status=HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response({"id" : serializer.data.get("id")}, status=HTTP_200_OK)


class BaseSingleView(BaseView):
    def get(self, request, id):
        entry = self.fetch_data(id)

        if not entry:
            return Response({"details" : "Resource is not found"}, status=HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(entry)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def put(self,request, id):
        entry = self.fetch_data(id)

        if not entry:
            return Response({"details" : "Resource is not found"}, status=HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(entry, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
        else:
            return Response({"details" : "Not appropriate request.", "errors" : serializer.errors}, status=HTTP_400_BAD_REQUEST)
        return Response({"id" : serializer.data.get("id")}, status=HTTP_200_OK)
        
    
    def delete(self, request, id):
        entry = self.fetch_data(id)

        if not entry:
            return Response({"details" : "Resource is not found"}, status=HTTP_404_NOT_FOUND)
        
        entry.delete()
        return Response({"details" : "No content"}, status=HTTP_204_NO_CONTENT)


class SingleProductView(BaseSingleView):
    model = Product
    serializer_class = ProductSerializer

class ManyProductView(BaseManyView):
    model = Product
    serializer_class = ProductSerializer


class SingleProductCategoryView(BaseSingleView):
    model = ProductCategory
    serializer_class = ProductCategorySerializer

class ManyProductCategoryView(BaseManyView):
    model = ProductCategory
    serializer_class = ProductCategorySerializer

@api_view(['GET'])
def products_by_category(self, id):
    products = Product.objects.filter(category=int(id))
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=HTTP_200_OK)
