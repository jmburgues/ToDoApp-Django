from django import forms
from . import models
from django.contrib.auth.models import User


# creates a form using django built in app forms and also using already created models
class CreateTask(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['title', 'body', 'state', 'assigned']

    assigned = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
