from django.db import models

# Create your models here.
from django.db.models import CASCADE

from tasks.models import Task


class Notification(models.Model):
    title = models.CharField(max_length=50)
    reason = models.CharField(max_length=200)
    reporter = models.ForeignKey(Task, on_delete=CASCADE)
    user = models.ManyToManyField(User, default=None)
    UNREAD = 'UNREAD'
    READ = 'READ'
    STATUS_CHOICES = [
        (UNREAD, 'Unread'),
        (READ, 'Read'),
    ]
    status = models.CharField(
        choices=STATUS_CHOICES,
        default=UNREAD,
        max_length=12
    )
    ALERT = 'ALERT'
    IMPORTANT = 'IMPORTANT'
    MUST = 'MUST'
    CRITICAL = 'CRITICAL'
    TYPE_CHOICES = [
        (ALERT, 'This is just an alert'),
        (IMPORTANT, 'This is very important '),
        (MUST, 'This must be done at the end of the day'),
        (CRITICAL, 'This is already delayed'),
    ]
    type = models.CharField(
        choices=TYPE_CHOICES,
        default=ALERT,
        max_length=12
    )

    def __str__(self):
        return self.title

    def snippet(self):
        if len(str(self.reason)) > 20:
            return self.body[0:20] + ' (...)'
        else:
            return self.body


