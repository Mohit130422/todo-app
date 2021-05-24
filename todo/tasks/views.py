from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.

def index(request):
    tsk = task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tsk': tsk, 'form': form}
    return render(request, 'tasks/list.html', context)


def update(request, pk):
    step = task.objects.get(id=pk)

    form = TaskForm(instance=step)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=step)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form': form}

    return render(request, 'tasks/update.html', context)


def delete(request, pk):
    item = task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')
    
    context= {'item':item}
    return render(request, 'tasks/delete.html', context)
