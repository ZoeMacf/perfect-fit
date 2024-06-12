from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import PuzzleExchange
from .forms import PuzzleExchangeForm



def puzzles(request):
    """ A view to show all puzzles, also sorting and filtering queries """

    puzzles = PuzzleExchange.objects.all()

    context = {
        'puzzles': puzzles,
    }

    return render(request, 'puzzle_exchange/puzzle_list.html', context)

def puzzle_detail(request, puzzle_id):
    """ view to render a detailed post for puzzle submission """

    puzzle = get_object_or_404(PuzzleExchange, pk=puzzle_id)
    context = {
        'puzzle':puzzle
    }

    return render(request, 'puzzle_exchange/puzzle_detail.html')

def user_submissions(request):
    """ view to render a list of users submissions """

    return render(request, 'puzzle_exchange/user_submissions.html')

def submit_puzzle(request):
    """ view to create a puzzle submit form """

    if request.method == 'POST':
        form = PuzzleExchangeForm(request.POST, request.FILES)
        if form.is_valid():
            puzzle = form.save(commit=False)
            puzzle.poster = request.user.userprofile
            puzzle = form.save()
            messages.success(request, 'Successfully submitted a puzzle!')
            return redirect(reverse('puzzle_list'))
        else: 
            messages.error(request, 'Failed to submit your puzzle. Please ensure the form is valid')
    else:
        form = PuzzleExchangeForm()

        template = 'puzzle_exchange/submit_puzzle.html'
        context = {
            'form':form
        }

    return render(request, template, context)