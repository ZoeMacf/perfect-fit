from django.urls import path
from . import views

urlpatterns = [
  path('', views.puzzle_exchange, name='puzzle_exchange'),
  path('puzzle_details/', views.puzzle_detail, name='puzzle_details'),
  path('user_submissions/', views.user_submissions, name='user_submissions'),
  path('submit_puzzle/', views.submit_puzzle, name='submit_puzzle')
]
