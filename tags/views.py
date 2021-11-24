from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Tag
from django.http import HttpResponse
from . import forms


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags/tag_list.html', {'tags': tags})


@login_required(login_url="/accounts/login/")
def tag_delete(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    tag.delete()
    return redirect('tags:admin')


@login_required(login_url="/accounts/login/")
def tag_admin(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        form = forms.CreateTag(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            if tag.title[0] != '#':
                tag.title = '#'+tag.title
            tag.save()
        return redirect('tasks:list')
    else:
        tags = Tag.objects.all()
        form = forms.CreateTag()
    return render(request, 'tags/tag_admin.html', {'form': form, 'tags': tags})
