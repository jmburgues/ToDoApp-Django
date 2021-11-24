from django import forms
from . import models


# creates a form using django built in app forms and also using already created models
class CreateTag(forms.ModelForm):
    class Meta:
        model = models.Tag
        fields = ['title']

