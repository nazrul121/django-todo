
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Welcome to About us page')
    return render(request, 'home.html')