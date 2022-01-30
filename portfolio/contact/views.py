from django.shortcuts import render

# Create your views here.

def contact(request):
    context = {}
    return render(request, 'context/context.html', context)
