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
        'title': 'Форум',
        'menu': menu,
        'posts': posts,
        'cats': cats,
    }
    return render(request, 'forum/forum.html', context)


def post_detail(request, post_id):
    post = Forum.objects.get(pk=post_id)
    context = {
        'title': 'Форум',
        'menu': menu,
        'post': post
    }
    return render(request, 'detail_post.html', context=context)

def category(request, cat_id):
    posts = Forum.objects.filter(pk=cat_id)
    cat = Category_forum.objects.get(pk=cat_id)
    context = {
        'title': 'Категории',
        'menu': menu,
        'cat': cat,
        'posts': cat,
    }
    return render(request, 'forum/show_category', context)
