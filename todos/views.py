from django.shortcuts import render, HttpResponse
from .models import Task
# Create your views here.

def addTask(request):
    if request.method == 'POST':

        task = request.POST.get('task')
        # return HttpResponse(request)
        Task.objects.create(task=task)
        return HttpResponse('Form has submitted')

    return HttpResponse('Only post method is allowed')