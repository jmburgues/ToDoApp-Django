from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Notification
from tasks.models import Task
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

# Create your views here.


def notification_list(request):
    notifications = Notification.objects.all()
    return render(request, 'notifications/notification-list.html', {'notifications': notifications})


@login_required(login_url="/accounts/login/")
def notification_details(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    task = Task.objects.get(notification=notification)
    return render(request, 'notifications/notification-details.html', {'notification': notification, 'task': task})


@login_required(login_url="/accounts/login/")
def notification_delete(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.delete()
    return redirect('notifications:list')


