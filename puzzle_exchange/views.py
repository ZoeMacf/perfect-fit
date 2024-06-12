from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import PuzzleExchange
from .forms import PuzzleExchangeForm



def puzzle_exchange(request):
    """ view to render the puzzle exchange page """

    return render(request, 'puzzle_exchange/puzzle_exchange.html')

def puzzle_detail(request):
    """ view to render a detailed post for puzzle submission """

    return render(request, 'puzzle_exchange/puzzle_details.html')

def user_submissions(request):
    """ view to render a list of users submissions """

    return render(request, 'puzzle_exchange/user_submissions.html')

def submit_puzzle(request):
    """ view to create a puzzle submit form """

    if request.method == 'POST':
        form = PuzzleExchangeForm(request.POST, request.FILES)
        if form.is_valid():
            puzzle = form.save(commit=False)
            puzzle.poster = poster
            puzzle = form.save()
            messages.success(request, 'Successfully submitted a puzzle!')
            return redirect(reverse('puzzle_exchange'))
        else: 
            messages.error(request, 'Failed to submut your puzzle. Please ensure the form is valid')
    else:
        form = PuzzleExchangeForm()

        template = 'puzzle_exchange/submit_puzzle.html'
        context = {
            'form':form
        }

    return render(request, template, context)