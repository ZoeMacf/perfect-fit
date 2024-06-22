from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .forms import ContactUsForm
from .models import ContactUs


def contact_us_query(request):
    """view to create and send a contact query"""

    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()

        if form.is_valid():
            query = form.save()
            confirm_query(query)
            return redirect(reverse("contact_success"))
        else:
            messages.error(
                request, "Failed to send query, '\
                please ensure the form is valid."
            )
    else:
        form = ContactUsForm()

    template = "contact_us/contact_us.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


def confirm_query(contact_us):
    """confirm query has been submitted"""

    cust_email = contact_us.email
    subject = render_to_string(
        "contact_us/contact_us_emails/contact_us_subject.txt",
        {"contact_us": contact_us},
    )
    body = render_to_string(
        "contact_us/contact_us_emails/contact_us_body.txt",
        {'contact_us':contact_us, "contact_email": settings.EMAIL_HOST_USER},
    )

    send_mail(subject, body, settings.EMAIL_HOST_USER, [cust_email])


def contact_success(request):

    template = "contact_us/contact_us_success.html"

    return render(request, template)
