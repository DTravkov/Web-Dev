from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ManyProductView, SingleProductView, ManyProductCategoryView, SingleProductCategoryView

urlpatterns = [
    path('products/', ManyProductView.as_view()),
    path('products/<int:id>', SingleProductView.as_view()),
    path('categories/', ManyProductCategoryView.as_view()),
    path('categories/<int:id>', SingleProductCategoryView.as_view()),
    path('categories/<int:id>/products', SingleProductCategoryView.as_view()),
    
]