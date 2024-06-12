from django.urls import path
from . import views

urlpatterns = [
    path('user_msgs/submit_message/', views.SubmitMessageView.as_view(), name="submit_message")
]