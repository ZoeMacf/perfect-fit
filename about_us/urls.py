from django.urls import path
from . import views

urlpatterns = [
  path('', views.view_about_us, name='about_us'),
]
