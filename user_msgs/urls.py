from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_message, name='submit_message')
]