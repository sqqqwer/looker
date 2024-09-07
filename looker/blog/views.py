from django.shortcuts import render
from django.views.generic import ListView


# class HomePage(ListView):

def home_page(request):
    template = 'base.html'
    return render(request, template)
