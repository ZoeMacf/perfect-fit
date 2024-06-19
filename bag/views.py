from django.shortcuts import (
    render, redirect, get_object_or_404, HttpResponse
)
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """view to render the shopping bag page"""

    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """Add a selected quantity of product to the bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    bag = request.session.get("bag", {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request, f"Updated {product.name} quantity to your {bag[item_id]}"
        )

    else:
        bag[item_id] = quantity
        messages.success(request, f"Added {product.name} to your bag")

    request.session["bag"] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Update the quantity of the bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    bag = request.session.get("bag", {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request, f"Updated quantity of {product.name} to {bag[item_id]}"
        )

    else:
        del bag[item_id]
        messages.success(request, f"Removed {product.name} from your bag")

    request.session["bag"] = bag
    return redirect(reverse("view_bag"))


def remove_item(request, item_id):
    """Remove an item from the bag"""

    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get("bag", {})

    try:
        bag.pop(item_id)
        messages.success(request, f"Removed {product.name} from your bag")

        request.session["bag"] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)
