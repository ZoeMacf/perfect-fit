from django.urls import path
from . import views

urlpatterns = [
    path("", views.contact_us_query, name="contact_us_query"),
    path("contact_us_success/", views.contact_success, name="contact_success"),
]
