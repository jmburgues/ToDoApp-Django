from django.shortcuts import render
from .models import  Notification


# Create your views here.


def notification_list(request):
    notifications = Notification.objects.all()
    return render(request, 'notifications/notification-list.html', {'notifications': notifications})


def notification_details(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    return render(request, 'notifications/notification-details.html', {'notification': notification})


