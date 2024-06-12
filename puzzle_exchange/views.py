from django.shortcuts import render



def view_puzzle_exchange(request):
    """ view to render the puzzle exchange page """

    return render(request, 'puzzle_exchange/puzzle_exchange.html')

def puzzle_detail(request):
    """ view to render a detailed post for puzzle submission """

    return render(request, 'puzzle_exchange/puzzle_details.html')

def user_submissions(request):
    """ view to render a list of users submissions """

    return render(request, 'puzzle_exchange/user_submissions.html')