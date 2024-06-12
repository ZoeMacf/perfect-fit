from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import PuzzleExchange
from .forms import PuzzleExchangeForm


@login_required
def puzzles(request):
    """ A view to show all puzzles, also sorting and filtering queries """

    puzzles = PuzzleExchange.objects.all()

    paginator = Paginator(puzzles, 3)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'puzzles': puzzles,
        'page_obj': page_obj
    }

    return render(request, 'puzzle_exchange/puzzle_list.html', context)

@login_required
def puzzle_detail(request, puzzle_id):
    """ view to render a detailed post for puzzle submission """

    puzzle = get_object_or_404(PuzzleExchange, pk=puzzle_id)
    context = {
        'puzzle':puzzle
    }

    return render(request, 'puzzle_exchange/puzzle_detail.html', context)

@login_required
def user_submissions(request):
    """ view to render a list of users submissions """

    puzzles = PuzzleExchange.objects.all()
    user_puzzles = puzzles.filter(poster=request.user.userprofile)

    template = 'puzzle_exchange/user_submissions.html'
    context = {
        'users_puzzles':user_puzzles
    }

    return render(request, template, context)

@login_required
def submit_puzzle(request):
    """ view to create a puzzle submit form """

    if request.method == 'POST':
        form = PuzzleExchangeForm(request.POST, request.FILES)
        if form.is_valid():
            puzzle = form.save(commit=False)
            puzzle.poster = request.user.userprofile
            puzzle = form.save()
            messages.success(request, 'Successfully submitted a puzzle!')
            return redirect(reverse('puzzle_detail', args=[puzzle.id]))
        else: 
            messages.error(request, 'Failed to submit your puzzle. Please ensure the form is valid')
    else:
        form = PuzzleExchangeForm()

        template = 'puzzle_exchange/submit_puzzle.html'
        context = {
            'form':form
        }

    return render(request, template, context)