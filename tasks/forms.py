from django import forms
from . import models
from django.contrib.auth.models import User
from .models import Tag


# creates a form using django built in app forms and also using already created models
class CreateTask(forms.ModelForm):
    class Meta:
        model = models.Task
        fields = ['title', 'body', 'tags', 'state', 'assigned']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'assigned': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
