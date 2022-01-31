from django.shortcuts import render

from .home_context import build_context

# Create your views here.

def home(request):
    context = build_context()
    return render(request, 'homepage/homepage.html', context)
