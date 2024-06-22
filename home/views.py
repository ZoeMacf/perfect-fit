from django.shortcuts import render


def index(request):
    """A view to return the main home page"""

    return render(request, "home/index.html")


def privacy_policy(request):
    """ View to return the privacy policy page"""

    return render(request, 'home/privacy_policy.html')