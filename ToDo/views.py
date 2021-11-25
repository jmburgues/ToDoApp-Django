from django.shortcuts import render
from tasks.models import Task


def homepage(request):

    notifications = Notification.objects.all()

    return render(request, 'homepage.html', {'notifications': notifications})

