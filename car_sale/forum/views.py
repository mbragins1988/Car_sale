from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from car.views import menu
from forum.models import *
from forum.forms import *


def forum(request):
    posts = Forum.objects.all()
    context = {
        'title': 'Форум сообщества Car sale',
        'menu': menu,
        'posts': posts,
        'cat_selected': 0,
        'flag_post': 'post',
    }
    return render(request, 'forum/forum.html', context)


def post_detail(request, post_slug):
    post = get_object_or_404(Forum, slug=post_slug)
    context = {
        'title': 'Форум сообщества Car sale',
        'menu': menu,
        'post': post,
        'cat_selected': post_slug,
        'flag_post': 'post',
    }
    return render(request, 'forum/detail_post.html', context=context)


def category(request, cat_slug):
    posts = Forum.objects.filter(cat__slug=cat_slug)
    context = {
        'title': 'Форум',
        'menu': menu,
        'posts': posts,
        'cat_selected': cat_slug,
        'flag_post': 'post',
    }
    return render(request, 'forum/forum.html', context)


def add_post(request):
    if request.method == "POST":
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('forum:forum')
    else:
        form = AddPostForm()

    context = {
        'title': 'Добавить пост',
        'menu': menu,
        'flag_post': 'post',
        'form': form,
    }
    return render(request, 'forum/add_post.html', context=context)
