from django.shortcuts import render


def index(request):
    context = {'title': 'Store title'}
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Products',
        'products': [
            {
                'image': '/static/vendor/img/products/Adidas-hoodie.png',
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': 6090,
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
            }
        ]
    }
    return render(request, 'products/product.html', context)
