from collections import Counter
from typing import Any, Dict
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, CreateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from forum.models import *
from forum.forms import *
from forum.utils import *


class ForumHome(DataMixin, ListView):
    paginate_by = 10
    model = Forum
    template_name = 'forum/forum.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


class PostDetail(DataMixin, DetailView):
    model = Forum
    template_name = 'forum/detail_post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class PostCategory(DataMixin, ListView):
    model = Forum
    template_name = 'forum/forum.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Forum.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория - ' + str(context['posts'][0].cat),
                                      cat_selected = context['posts'][0].cat.slug)
        return dict(list(context.items()) + list(c_def.items()))


class AddPost(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'forum/add_post.html'
    success_url = reverse_lazy('forum:forum')
    login_url = reverse_lazy('forum:forum')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить пост', cat_selected = None)
        return dict(list(context.items()) + list(c_def.items()))
