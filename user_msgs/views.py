from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserMessage
from .forms import MessageForm

def submit_message(request):
    """ view to create a puzzle submit form """

    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user.userprofile
            puzzle = form.save()
            messages.success(request, 'Successfully sent message to user!')
            return redirect(reverse('puzzle_detail', args=[puzzle.id]))
        else: 
            messages.error(request, 'Failed to submit your message. Please ensure the form is valid')
    else:
        form = MessageForm()

        template = 'user_msgs/submit_message.html'
        context = {
            'form':form
        }

    return render(request, template, context)