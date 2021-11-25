from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'tags'

urlpatterns = [
    url(r'^$', views.tag_list, name='list'),
    url(r'^admin/$', views.tag_admin, name='admin'),
    url(r'^(?P<tag_id>[0-9]+)/delete/$', views.tag_delete, name='delete'),
]
