from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ManyProductView, SingleProductView, ManyCategoryView, SingleCategoryView

urlpatterns = [
    path('products/', ManyProductView.as_view()),
    path('products/<int:id>', SingleProductView.as_view()),
    path('categories/', ManyCategoryView.as_view()),
    path('categories/<int:id>/products', SingleCategoryView.as_view()),
]