from django.db import models


# more info on model types on https://docs.djangoproject.com/en/1.11/ref/models/fields
class Task(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)  # automatically populates date when constructed.
    IN_PROGRESS = 'P'
    FINISHED = 'F'
    STATE_CHOICES = (
        (IN_PROGRESS, 'In Progress'),
        (FINISHED, 'Finished'),
    )
    state = models.CharField(
        max_length=2,
        choices=STATE_CHOICES,
        default=IN_PROGRESS,
    )
    # add in tag list

    def __str__(self):
        return self.title
