from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    return products page, show all products with sorting and search queries
    """

    # filter only active products
    products = Product.objects.filter(is_active=True)

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)