from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductList.as_view(), name='product_list'),
    path('product/<int:pk>', ProductDetail.as_view(), name='product_detail'),
]