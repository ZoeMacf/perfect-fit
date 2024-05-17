from django.shortcuts import render, get_object_or_404

from .models import Product

# Create your views here.

def all_products(request):
  """ A view to display all of the products available"""

  products = Product.objects.all()

  context = {
        'products': products
    }

  return render(request, 'products/all_products.html', context)
  

def product_detail(request, product_id):
    """ A view for an individual product information """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
