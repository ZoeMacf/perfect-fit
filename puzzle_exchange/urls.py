from django.urls import path
from . import views

urlpatterns = [
  path('', views.view_puzzle_exchange, name='puzzle_exchange'),
  path('puzzle_details/', views.puzzle_detail, name='puzzle_details'),
  path('user_submissions/', views.user_submissions, name='user_submissions')
]
