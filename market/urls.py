from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductList.as_view(), name='products'),
    path('category/<int:pk>', ProductsOfCategory.as_view(), name='products_of_category'),
    # path('product/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('product/<int:pk>', product_detail, name='product_detail'),
    path('order_create/', order_create, name='order_create'),
    # path('logout/', LogoutView.as_view(template_name='market/logout.html'), name='log_out'),
    path('logout/', logout_view, name='logout'),
    path('cabinet/', CabinetView.as_view(), name='cabinet'),
    path('data_create/', DataCreate.as_view(), name='data_create'),
    path('comment/<int:pk>', comment_add, name='comment_add'),
    path('about/', AboutView.as_view(), name='about'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('/', ContactView.as_view(), name='index'), #dopil
    path('login/', ContactView.as_view(), name='log'),
    path('checkout/', ContactView.as_view(), name='checkout'),
    path('catalog/', ContactView.as_view(), name='catalog'),
]