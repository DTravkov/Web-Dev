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
from auth.views import AuthViewSet

from api.views import ProductViewSet, CategoryViewSet

auth_router = routers.SimpleRouter()
auth_router.register('auth', AuthViewSet, basename='auth')

product_api_router = routers.DefaultRouter()
product_api_router.register('api/products', ProductViewSet, basename='api')

category_api_router = routers.DefaultRouter()
category_api_router.register('api/categories', CategoryViewSet, basename='api')

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += auth_router.urls
urlpatterns += product_api_router.urls
urlpatterns += category_api_router.urls