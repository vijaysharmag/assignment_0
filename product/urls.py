from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from product import views



router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')


urlpatterns = [
    path('', include(router.urls)),
    
]   