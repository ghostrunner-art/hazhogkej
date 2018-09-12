from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    context = {}
    context['hello'] = 'world!'
    return render(request, 'index.html', context)
