from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Product, Category, Reviews
from .forms import ProductForm, ReviewForm

# Create your views here.

def products(request):
    """ A view to show all puzzles, also sorting and filtering queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    paginator = Paginator(products, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
   

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'page_obj': page_obj
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """ A view for an individual product information """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def add_product(request):
    """ add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product to store!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product to store. Please ensure the form is valid')
    else:
        form = ProductForm()

        
    template = 'products/add_product.html'
    context = {
        'form':form
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit an existing product """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully update product information!')
            return redirect(reverse('product_detail', args=[product.id]))
        else: 
            messages.error(request, 'Failed to update product information. Please ensure the form is valid')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form':form,
        'product':product
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store"""

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
    

def add_review(request, product_id):
  """ add a review to product"""
  product = get_object_or_404(Product, pk=product_id)
  if request.method == 'POST':
    form = ReviewForm(request.POST, request.FILES)
    if form.is_valid():
        review = form.save(commit=False)
        review.author = request.user.userprofile
        review.product = product
        review = form.save()
        messages.success(request, 'Successfully submitted your review!')
        return redirect(reverse('product_detail', args=[product.id]))
    else:
        messages.error(request, 'Failed to submit your review. Please ensure the form is valid')
  else:
    form = ReviewForm()

    template = 'products/add_review.html'
    context  = {
    'form': form,
    'product':product
    }

    return render(request, template, context)