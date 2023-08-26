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


def forum(request):
    posts = Forum.objects.all()
    cats = Category_forum.objects.all()
    context = {
        'title': 'Форум сообщества Car sale',
        'menu': menu,
        'posts': posts,
        'cats': cats,
        'cat_selected': 0,
    }
    return render(request, 'forum/forum.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Forum, pk=post_id)
    cats = Category_forum.objects.all()
    context = {
        'title': 'Форум',
        'menu': menu,
        'post': post,
        'cats': cats,
    }
    return render(request, 'forum/detail_post.html', context=context)

def category(request, cat_id):
    posts = Forum.objects.filter(pk=cat_id)
    cats = Category_forum.objects.all()
    context = {
        'title': 'Категории',
        'menu': menu,
        'cats': cats,
        'posts': posts,
        'cat_selected': cat_id
    }
    return render(request, 'forum/show_category.html', context)
