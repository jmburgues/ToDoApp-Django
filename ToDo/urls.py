from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from tasks import views as task_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # regex for paths that start with 'accounts/'
    # include('accounts.urls') includes the paths declared un accounts/urls.py so they can be matched.
    # same for tasks
    url(r'^accounts/', include('accounts.urls')),
    url(r'^tasks/', include('tasks.urls')),
    url(r'^tags/', include('tags.urls')),
    url(r'^notifications/', include('notifications.urls')),
    url(r'^$', task_views.task_list, name="home")
]

urlpatterns += staticfiles_urlpatterns()  # for adding static files to urls (style.css)
