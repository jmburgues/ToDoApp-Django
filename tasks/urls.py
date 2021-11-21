from django.conf.urls import url
from . import views

app_name = 'tasks'

urlpatterns = [
    url(r'^$', views.task_list, name='list'),
    url(r'^create/$', views.task_create, name='create'),
    # (?P<task_id>[0-9]+) format (?P<VARIABLE>REGEX) specifies the regex for that variable and that will be passed to
    # the view fun. For name='detail' is a name given to reference the URL created dynamically (used on tasks_list.html)
    url(r'^(?P<task_id>[0-9]+)/$', views.task_details, name='detail'),
]
