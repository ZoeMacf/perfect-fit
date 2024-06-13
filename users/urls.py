from django.urls import path
from . import views

urlpatterns = [
  path('', views.user_profile, name='user_profile'),
  path('order_detail/<order_number>', views.order_detail, name='order_detail'),

]