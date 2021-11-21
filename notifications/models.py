from django.db import models

# Create your models here.
from tasks.models import Task


class Notification(models.Model):
    title = models.CharField(max_length=50)
    reason = models.CharField(max_length=200)
    reporter = models.ForeignKey(Task)
    TYPE_CHOICES = [
        (ALERT, 'This is just an alert'),
        (IMPORTANT, 'This is very important '),
        (MUST, 'This must be done at the end of the day'),
        (CRITICAL, 'This is already delayed'),
    ]
    type = models.CharField(
        choices=TYPE_CHOICES,
        default=ALERT,
    )


