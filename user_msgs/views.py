from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import View

from .models import UserMessage


class SubmitMessageView(View):

    def post(self, request, *args, **kwargs):

        receiver_id = request.POST.get('receiver_id', '')
        file = request.FILES.get('file', '')
        UserMessage.objects.create(sender=request.user, receiver__id=receiver_id, message_file=file)
        return render(request,)