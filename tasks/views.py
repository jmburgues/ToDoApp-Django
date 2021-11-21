from django.shortcuts import render
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks_list.html', {'tasks': tasks})