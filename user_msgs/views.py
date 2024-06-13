from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from .models import UserMessage
from puzzle_exchange.models import PuzzleExchange
from .forms import UserMessageForm


@login_required
def submit_message(request, puzzle_id):

    puzzle = get_object_or_404(PuzzleExchange, pk=puzzle_id)

    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user.userprofile
            message.receiver = puzzle.poster.user.userprofile
            message = form.save()
            messages.success(request, f'Successfully sent your message to {puzzle.poster}!')
            return redirect(reverse('message_success', args=[puzzle.id]))
        else:
            messages.error(request, 'Failed to submit your message. Please ensure the form is valid')
    else:
        form = UserMessageForm()

    template = 'user_msgs/submit_message.html'
    context  = {
    'form': form,
    'puzzle':puzzle
    }

    return render(request, template, context)

def message_success(request, puzzle_id):
    """ view to show sucessful message sent """

    puzzle = get_object_or_404(PuzzleExchange, pk=puzzle_id)
    

    template = 'user_msgs/message_success.html'
    context = {
        'puzzle':puzzle
    }

    return render(request, template, context)
