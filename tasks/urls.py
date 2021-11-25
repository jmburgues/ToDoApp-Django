from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    url(r'^$', views.task_list, name='list'),
    url(r'^json$', views.task_to_json, name='task_list'),
    url(r'^create/$', views.task_create, name='create'),
    url(r'^(?P<task_id>[0-9]+)/state/$', views.task_change_state, name='change_state'),
    url(r'^(?P<task_id>[0-9]+)/delete/$', views.task_delete, name='delete'),
    url(r'^(?P<task_id>[0-9]+)/update/$', views.task_update, name='update'),
    url(r'^(?P<id>[0-9]+)/filter/$', views.task_filter, name='filter'),
    # (?P<task_id>[0-9]+) format (?P<VARIABLE>REGEX) specifies the regex for that variable and that will be passed to
    # the view fun. For name='detail' is a name given to reference the URL created dynamically (used on tasks_list.html)
    url(r'^(?P<task_id>[0-9]+)/$', views.task_details, name='detail'),
]
