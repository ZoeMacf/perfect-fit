from django.urls import path
from . import views

urlpatterns = [
  path('', views.view_puzzle_exchange, name='puzzle_exchange'),
]
