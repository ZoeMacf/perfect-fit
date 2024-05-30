from django.shortcuts import render



def view_about_us(request):
    """ view to render the about us page """

    return render(request, 'about_us/about_us.html')