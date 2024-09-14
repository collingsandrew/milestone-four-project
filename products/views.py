from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    """
    return products page, show all products with sorting and search queries
    """

    # filter only active products
    products = Product.objects.filter(is_active=True)
    query = None
    categories = None
    is_favourite = False

    if request.GET:
        # filter favourite products
        if 'is_favourite' in request.GET:
            is_favourite = request.GET['is_favourite'].lower() == 'true'
            products = products.filter(is_favourite=is_favourite)

        # filter products by categories
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # filter products based on search
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request,"You didn't enter any search criteria!"
                )
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) |
                Q(author__icontains=query) |
                Q(format_type__icontains=query) |
                Q(isbn__icontains=query)
            )
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'is_favourite': is_favourite,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    return product details page
    """

    # filter only active products
    product = get_object_or_404(Product, id=product_id, is_active=True)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
