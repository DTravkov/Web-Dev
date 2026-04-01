"""
URL configuration for shopBack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

# imported from __init__ fiel
from api.views import ProductDetailAPIView, ProductListAPIView, CategoryListAPIView, CategoryDetailAPIView

from auth.views import AuthViewSet

auth_router = routers.SimpleRouter()
auth_router.register('auth', AuthViewSet, basename='auth')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/products/", ProductListAPIView.as_view()),
    path("api/products/<int:product_id>/", ProductDetailAPIView.as_view()),
    path("api/categories/", CategoryListAPIView.as_view()),
    path("api/categories/<int:category_id>/", CategoryDetailAPIView.as_view()),
]

urlpatterns += auth_router.urls

