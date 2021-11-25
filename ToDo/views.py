from django.shortcuts import render
from notifications.models import Notification


def homepage(request):
    return render(request, 'homepage.html', {'notifications': count})

