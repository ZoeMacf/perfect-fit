from django.shortcuts import render

def index(request):
    """A view to return the main home page"""

    return render(request, 'home/index.html')
