from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ProductCategorySerializer, ProductSerializer
from .models import Product, ProductCategory
from .utils import ResponseTemplates




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

        return ResponseTemplates.ok(data=serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
        else:
            return ResponseTemplates.bad_request(errors=serializer.errors)

        return ResponseTemplates.ok(data=[{"id" : serializer.data.get("id")}])


class BaseSingleView(BaseView):
    def get(self, request, id):
        entry = self.fetch_data(id)

        if not entry:
            return ResponseTemplates.not_found()
        
        serializer = self.serializer_class(entry)
        return ResponseTemplates.ok(data=[serializer.data])
    
    def put(self,request, id):
        entry = self.fetch_data(id)

        if not entry:
            return ResponseTemplates.not_found()
        
        serializer = self.serializer_class(entry, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
        else:
            return ResponseTemplates.bad_request(errors=serializer.errors)
        return ResponseTemplates.ok(data=[{"id" : serializer.data.get("id")}])
        
    
    def delete(self, request, id):
        entry = self.fetch_data(id)

        if not entry:
            return ResponseTemplates.not_found()
        
        entry.delete()
        return ResponseTemplates.no_content()


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