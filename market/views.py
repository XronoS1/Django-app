from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from .forms import ProductForm
# Create your views here.


class ProductList(ListView):
    model = Product
    template_name = 'product_list'  #имя тимплэйта
    context_object_name = 'products' #как обращаться в тимплэйте


class ProductDetail(DetailView):
    form_class = ProductForm
    model = Product
    template_name = 'product'  # имя тимплэйта
    context_object_name = 'product'  # как обращаться в тимплэйте