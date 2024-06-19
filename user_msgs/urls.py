from django.urls import path
from . import views

urlpatterns = [
    path(
        "user_msgs/submit_message/<int:puzzle_id>/",
        views.submit_message,
        name="submit_message",
    ),
    path(
        "user_msgs/message_success/<int:puzzle_id>/",
        views.message_success,
        name="message_success",
    ),
]
