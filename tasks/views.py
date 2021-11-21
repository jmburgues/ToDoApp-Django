from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from . import forms


def task_list(request):
    tasks = Task.objects.all()  # we can append here .order_by('date') or any other.
    return render(request, 'tasks/tasks_list.html', {'tasks': tasks})


def task_details(request, task_id):
    task = Task.objects.get(id=task_id)
    # Render a template and send data to it.
    # Pass the variable task created to the template with {'task': task}
    return render(request, 'tasks/task_detail.html', {'task': task})


# login decorator prevents unauthenticated users
@login_required(login_url="/accounts/login/")
def task_create(request):
    if request.method == 'POST':
        form = forms.CreateTask(request.POST)  # creates a form with data coming from the request
        if form.is_valid():
            form.save()
        return redirect('tasks:list')
    else:
        form = forms.CreateTask()  # creates a form object from tasks/forms.py
    return render(request, 'tasks/task_create.html', {'form': form})
