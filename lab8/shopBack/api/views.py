from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProductCategorySerializer, ProductSerializer
from .models import Product, ProductCategory


class BaseProductView:
    def fetch_product_data(self,id):
        product = None
        try:
            product = Product.objects.get(pk=id)
        except:
            product = None
        
        return product
    


class ManyProductView(APIView, BaseProductView):
    def get(self, request):
        products_list = Product.objects.all()
        serializer = ProductSerializer(products_list, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    


class SingleProductView(APIView, BaseProductView):
    def get(self, request, id):
        product = self.fetch_product_data(id)

        if not product:
            return Response(data={"status" : "N/A"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self,request, id):
        product = self.fetch_product_data(id)

        if not product:
            return Response(data={"status" : "N/A"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response({"status" : "OK"}, status=status.HTTP_200_OK)
        
    
    def delete(self, request, id):
        product = self.fetch_product_data(id)

        if not product:
            return Response({"status" : "N/A"}, status=status.HTTP_404_NOT_FOUND)
        
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class BaseCategoryView:
    def fetch_category_data(self,id):
        product = None
        try:
            product = ProductCategory.objects.get(pk=id)
        except:
            product = None
        
        return product
    


class ManyCategoryView(APIView, BaseCategoryView):
    def get(self, request):
        category_list = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(category_list, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductCategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
    


class SingleCategoryView(APIView, BaseCategoryView):
    def get(self, request, id):
        category = self.fetch_category_data(id)

        if not category:
            return Response(data={"status" : "N/A"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductCategorySerializer(category)
        return Response(serializer.data)
    
    def put(self,request, id):
        category = self.fetch_category_data(id)

        if not category:
            return Response(data={"status" : "N/A"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductCategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response({"status" : "OK"}, status=status.HTTP_200_OK)
        
    
    def delete(self, request, id):
        product = self.fetch_category_data(id)

        if not product:
            return Response({"status" : "N/A"}, status=status.HTTP_404_NOT_FOUND)
        
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
