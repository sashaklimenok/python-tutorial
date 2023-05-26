from django.shortcuts import render
from products.models import ProductCategory, Product


def index(request):
    context = {'title': 'Store title'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Products',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/product.html', context)
