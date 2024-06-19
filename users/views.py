from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import UserProfile
from .forms import UserProfileForm

from user_msgs.models import UserMessage
from user_msgs.forms import UserMessageForm
from puzzle_exchange.models import PuzzleExchange

from checkout.models import Order


@login_required
def user_profile(request):
    """display user profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Update failed. '\
            Please ensure the form is valid")
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = "users/user_profile.html"
    context = {
        "form": form,
        "orders": orders,
        "on_profile_page": True,
    }

    return render(request, template, context)


@login_required
def order_detail(request, order_number):
    """display users order in detail"""

    order = get_object_or_404(Order, order_number=order_number)

    template = "users/order_detail.html"
    context = {
        "order": order,
    }

    return render(request, template, context)


@login_required
def user_notifications(request):
    """ " view to show all of the user notifications"""

    all_messages = UserMessage.objects.all()
    user_messages = all_messages.filter(
        message_receiver=request.user.userprofile)
    message_receiver = request.user.userprofile

    template = "users/user_notifications.html"
    context = {"all_messages": all_messages, "user_messages": user_messages}

    return render(request, template, context)
