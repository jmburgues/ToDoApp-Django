from django.http import HttpResponse


def create(request):
    return HttpResponse('create')


def homepage(request):
    return HttpResponse('homepage')