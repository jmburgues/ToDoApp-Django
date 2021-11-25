from django.db import models
from django.contrib.auth.models import User
from tags.models import Tag


# more info on model types on https://docs.djangoproject.com/en/1.11/ref/models/fields
class Task(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)  # automatically populates date when constructed.
    assigned = models.ManyToManyField(User, default=None)
    tags = models.ManyToManyField(Tag, blank=True)
    IN_PROGRESS = 'IN PROGRESS'
    FINISHED = 'FINISHED'
    STATE_CHOICES = (
        (IN_PROGRESS, 'In Progress'),
        (FINISHED, 'Finished'),
    )
    state = models.CharField(
        max_length=12,
        choices=STATE_CHOICES,
        default=IN_PROGRESS,
    )

    # add in tag list

    def __str__(self):
        return self.title

    def snippet(self):
        if len(str(self.body)) > 40:
            return self.body[0:40] + ' (...)'
        else:
            return self.body



