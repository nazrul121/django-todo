from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Task
# Create your views here.

def addTask(request):
    if request.method == 'POST':

        task = request.POST.get('task')
        # return HttpResponse(request)
        Task.objects.create(task=task)
        return redirect('home')

    return HttpResponse('Only post method is allowed')



def markAsDone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def editTask(request, pk):
    task = get_object_or_404(Task, pk=pk)

    data = {
        'item': task,
    }

    # return HttpResponse(data)  

    return render(request, 'edit_task.html', data)


def updateTask(request, pk):
    if(request.method=='POST'):
        task = get_object_or_404(Task, pk=pk)
        # return HttpResponse(task)  
        task.task = request.POST.get('task')
        task.save()
        return redirect('home')
    else:
        return redirect('home')


def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')
    