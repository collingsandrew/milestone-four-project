from django.shortcuts import render


def index(request):
    """
    return the index page
    """
    return render(request, 'home/index.html')
