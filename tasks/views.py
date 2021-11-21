from django.shortcuts import render
from .models import Task
from django.http import HttpResponse


def task_list(request):
    tasks = Task.objects.all()  # we can append here .order_by('date') or any other.
    return render(request, 'tasks/tasks_list.html', {'tasks': tasks})


def task_details(request, task_id):
    task = Task.objects.get(id=task_id)
    # Render a template and send data to it.
    # Pass the variable task created to the template with {'task': task}
    return render(request, 'tasks/task_detail.html', {'task': task})
