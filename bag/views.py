from django.shortcuts import render


def view_bag(request):
    """
    return the bag page
    """
    
    return render(request, 'bag/bag.html')