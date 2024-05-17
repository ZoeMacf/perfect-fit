from django.shortcuts import render

from .models import Product

# Create your views here.

def all_products(request):
  """ A view to display all of the products available"""

  products = Product.objects.all()

  context = {
        'products': products
    }

  return render(request, 'products/all_products.html', context)
