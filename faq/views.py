from django.shortcuts import render


def view_faq(request):
    """view to render the faq page"""

    return render(request, "faq/faq.html")
