from django.contrib import admin
from django.urls import path

from .views import ProductsViewset, UserAPIView

urlpatterns = [
    path('products', ProductsViewset.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', ProductsViewset.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user', UserAPIView.as_view()),
]
