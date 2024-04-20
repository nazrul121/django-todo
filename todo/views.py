
from django.http import HttpResponse
from django.shortcuts import render
from todos.models import Task

def home(request):
    # return HttpResponse('Welcome to About us page')
    tasks = Task.objects.filter(is_completed=True)
    pendingTask = Task.objects.filter(is_completed=False).order_by('-modified_at')
    # return HttpResponse(tasks)
    data = {
        'tasks':tasks,
        'pendingTask': pendingTask
    }
    return render(request, 'home.html', data)