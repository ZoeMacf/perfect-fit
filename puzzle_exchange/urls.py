from django.urls import path
from . import views

urlpatterns = [
  path('', views.puzzles, name='puzzles'),
  path('<int:puzzle_id>/', views.puzzle_detail, name='puzzle_detail'),
  path('submit_puzzle/', views.submit_puzzle, name='submit_puzzle'),
  path('user_submissions/', views.user_submissions, name='user_submissions')
]
