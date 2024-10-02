from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product
from .models import Wishlist
from profiles.models import UserProfile


@login_required
def view_wishlist(request):
    """
    return the user's wishlist page
    """

    # get the user's profile and wishlist
    user_profile = get_object_or_404(
        UserProfile,
        user=request.user
    )
    # if the user does not have a wishlist, create one
    wishlist, created = Wishlist.objects.get_or_create(
        user_profile=user_profile
    )

    wishlist_items = wishlist.products.all()

    context = {
        'wishlist_items': wishlist_items,
    }

    return render(request, 'wishlist/wishlist.html', context)


@login_required
def add_to_wishlist(request, product_id):
    """
    add a product to the user's wishlist
    """
    product = get_object_or_404(Product, pk=product_id)
    
    # get the user's wishlist or create one if the user does not have one
    wishlist, created = Wishlist.objects.get_or_create(
        user_profile=request.user.userprofile
    )
    
    # check if the user has the product in their wishlist, if not then add it
    if product in wishlist.products.all():
        messages.info(
            request,
            f'{product.name} is already in your wishlist.'
        )
    else:
        wishlist.products.add(product)
        messages.success(
            request,
            f'Added {product.name} to your wishlist.'
        )
    
    return redirect('view_wishlist')


@login_required
def remove_from_wishlist(request, product_id):
    """
    remove a product from the user's wishlist
    """
    product = get_object_or_404(Product, pk=product_id)

    try:
        # get the users wishlist
        wishlist = get_object_or_404(
            Wishlist,
            user_profile=request.user.userprofile
        )
        
        # remove the product from the wishlist
        wishlist.products.remove(product)
        messages.success(
            request,
            f'Removed {product.name} from your wishlist.'
        )

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')

    return redirect('view_wishlist')
