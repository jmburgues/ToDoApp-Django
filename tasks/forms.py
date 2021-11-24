from django import forms
from . import models
from django.contrib.auth.models import User
from .models import Tag


# creates a form using django built in app forms and also using already created models
class CreateTask(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['title', 'body', 'tags', 'state', 'assigned']

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
