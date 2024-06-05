from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
  bag = request.session.get('bag', {})
  if not bag:
    messages.error(request, "There's nothing in your bag at the moment")
    return redirect(reverse('all_products'))

  order_form = OrderForm()
  template = 'checkout/checkout.html'
  context = {
    'order_form': order_form,
    'strip_public_key': 'pk_test_51P4qg4RwxIHzgK5BFrXtx5F8EPyKpNbEW6Ntr2ZQNSCA0quhsPPpz01Uw8pH7yLOD4912ojRXb4jNjlX7ypAcKyR00n3LrSaXW',
    'client_secret': 'test client secret',
  }

  return render(request, template, context)
