from django.shortcuts import render

def user_profile(request):
  """ display user profile"""
  template = 'users/profile.html'
  context = {}

  return render(request, template, context)
