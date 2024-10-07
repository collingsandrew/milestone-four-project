from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg
from datetime import date, timedelta

from .models import Product, Category, Review
from wishlist.models import Wishlist
from .forms import ProductForm, ReviewForm


def all_products(request):
    """
    return products page, show all products with sorting and search queries
    """

    # filter only active products
    products = Product.objects.filter(is_active=True)

    # calculate the average rating for each product
    products = products.annotate(average_rating=Avg('review__rating'))

    sort = None
    query = None
    categories = None
    is_favourite = False
    is_new_release = False

    if request.GET:
        # sorting of products
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort_field, sort_direction = sortkey.split('-')

            if sort_field == 'rating':
                sort_field = 'average_rating'

            if sort_direction == 'desc':
                sort_field = f'-{sort_field}'

            products = products.order_by(sort_field)
            sort = sortkey

        # filter new releases
        if 'is_new_release' in request.GET:
            is_new_release = request.GET['is_new_release'].lower() == 'true'
            if is_new_release:
                # get todays date
                start_date = date.today()
                # work out the date 60 days ago
                end_date = start_date - timedelta(days=60)
                # filter products based on the 60 day date range
                products = products.filter(
                    publication_date__range=(end_date, start_date)
                )

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
        'is_new_release': is_new_release,
        'sort': sort,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    return product details page
    """

    # filter only active products
    product = get_object_or_404(Product, id=product_id, is_active=True)

    reviews = product.review.all()

    # work out the average of all of the ratings for the product
    if reviews.exists():
        total_rating = sum(review.rating for review in reviews)
        average_rating = total_rating / reviews.count()
    else:
        average_rating = 'No Reviews'

    wishlist = None
    if request.user.is_authenticated:
        wishlist = Wishlist.objects.filter(
            user_profile=request.user.userprofile
            ).first()

    context = {
        'product': product,
        'wishlist': wishlist,
        'average_rating': average_rating,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Add a product to the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm()
    
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Successfully updated product!'
            )
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """
    add a review for a product
    """
    product = get_object_or_404(Product, id=product_id)
    if not request.user.is_authenticated:        
        messages.warning(
            request,
            'Please register/login to leave a review'
        )

        return redirect(reverse('product_detail', args=[product_id]))
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            # check if the user has already submitted a review
            if Review.objects.filter(
                user=request.user,
                product=product).exists():
                messages.error(
                    request,
                    "You have already submitted a review for this book"
                )
                return redirect(reverse('product_detail', args=[product_id]))

            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            messages.success(
                request,
                'Review submitted'
            )
            
            return redirect(reverse('product_detail', args=[product_id]))
    else:
        form = ReviewForm()

    template = 'products/add_review.html'
    context = {
        'form': form,
        'product': product
    }
    
    return render(request, template, context)
