from django.shortcuts import render



def view_puzzle_exchange(request):
    """ view to render the puzzle exchange page """

    return render(request, 'puzzle_exchange/puzzle_exchange.html')