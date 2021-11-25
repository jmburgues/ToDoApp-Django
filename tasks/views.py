from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core import serializers as deserialize
from .models import Task
from tags.models import Tag
from django.contrib.auth.models import User
from . import forms
import json
from rest_framework import serializers
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from notifications.models import Notification


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        model = Tag


# Necessary classes to serialize nested objects
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['username']
        model = User


class TaskSerializer(serializers.ModelSerializer):
    assigned = UserSerializer(read_only=True, many=True)
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        fields = '__all__'
        model = Task


def task_list(request):
    tasks = Task.objects.prefetch_related('assigned')
    assigned_tasks = []
    for task in tasks:
        for user in task.assigned.all():
            if user.id == request.user.id:
                assigned_tasks.append(task)

    notifications = Notification.objects.prefetch_related('users')
    count = 0
    for notification in notifications:
        for user in notification.users.all():
            if user.id == request.user.id:
                if notification.status == 'UNREAD':
                    count += 1

    return render(request, 'tasks/tasks_list.html', {'tasks': tasks, 'count': count})


def task_filter(request, id):
    tasks = Task.objects.prefetch_related('assigned').order_by('date')
    assigned_tasks = []
    filteredList = []
    for task in tasks:
        for user in task.assigned.all():
            if user.id == request.user.id:
                assigned_tasks.append(task)

    for task in assigned_tasks:
        tags = task.tags.all()
        for tag in tags:
            if int(tag.id) == int(id):
                filteredList.append(task)

    notifications = Notification.objects.prefetch_related('users')
    count = 0
    for notification in notifications:
        for user in notification.users.all():
            if user.id == request.user.id:
                if notification.status == 'UNREAD':
                    count += 1

    return render(request, 'tasks/tasks_list.html', {'tasks': filteredList, 'count': count})


def task_to_json(request):  # json endpoint for all tasks
    if request.method == 'GET':
        tasks = Task.objects.all()
        data = TaskSerializer(tasks, many=True).data
        return HttpResponse(json.dumps(data))  # json.dump converts dictionary to json


def task_details(request, task_id):
    task = Task.objects.get(id=task_id)
    # Render a template and send data to it.
    # Pass the variable task created to the template with {'task': task}
    return render(request, 'tasks/task_detail.html', {'task': task})


@login_required(login_url="/accounts/login/")
def task_change_state(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.state == task.IN_PROGRESS:
        Notification.notify_user(task, "FINISHED")
        task.state = task.FINISHED
    else:
        task.state = task.IN_PROGRESS
        Notification.notify_user(task, "IN PROGRESS")
    task.save()

    return redirect('tasks:list')


@login_required(login_url="/accounts/login/")
def task_delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    Notification.notify_user(task, "DELETED")
    return redirect('tasks:list')


@login_required(login_url="/accounts/login/")
def task_update(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        form = forms.CreateTask(request.POST, instance=task)  # creates a form with data coming from the request
        if form.is_valid():
            obj = form.save(commit=False)
            userIds = request.POST.getlist('assigned')
            obj.assigned.set(userIds)
            tagIds = request.POST.getlist('tags')
            obj.tags.set(tagIds)
            obj.save()
            Notification.notify_user(task, "UPDATED")
            return redirect('tasks:list')
    else:
        task = Task.objects.get(id=task_id)
        form = forms.CreateTask(initial={
            'id': task_id,
            'title': task.title,
            'body': task.body,
            'state': task.state,
            'assigned': task.assigned.all(),
            'tags': task.tags.all(),
        })  # creates a form object from tasks/forms.py
    return render(request, 'tasks/task_update.html', {'form': form, 'task': task})


# login decorator prevents unauthenticated users
@login_required(login_url="/accounts/login/")
def task_create(request):
    if request.method == 'POST':
        form = forms.CreateTask(request.POST)  # creates a form with data coming from the request
        if form.is_valid():
            task = form.save()
            print(request.user.id)
            Notification.notify_user(task, "CREATED")
        return redirect('tasks:list')
    else:
        form = forms.CreateTask()  # creates a form object from tasks/forms.py
    return render(request, 'tasks/task_create.html', {'form': form})
