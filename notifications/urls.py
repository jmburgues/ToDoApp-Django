from django.conf.urls import url
from . import views

app_name = 'notifications'

urlpatterns = [
    url(r'^$', views.notification_list, name='list'),
    url(r'^(?P<notification_id>[0-9]+)/delete/$', views.notification_delete, name='delete'),
    url(r'^(?P<notification_id>[0-9]+)/$', views.notification_details, name='detail'),
]

