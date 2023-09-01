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
from car.views import menu
from forum.models import *
from forum.forms import *


class ForumHome(ListView):
    model = Forum
    template_name = 'forum/forum.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['cat_selected'] = 0
        context['title'] = 'Форум сообщества Car sale'
        context['flag_post'] = 'post'
        return context


class PostDetail(DetailView):
    model = Forum
    template_name = 'forum/detail_post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        context['flag_post'] = 'post'
        return context


class PostCategory(ListView):
    model = Forum
    template_name = 'forum/forum.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Forum.objects.filter(cat__slug=self.kwargs['cat_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat.slug
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['flag_post'] = 'post'
        return context


class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'forum/add_post.html'
    success_url = reverse_lazy('forum:forum')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавить пост'
        context['flag_post'] = 'post',
        return context

# def add_post(request):
#     if request.method == "POST":
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('forum:forum')
#     else:
#         form = AddPostForm()

#     context = {
#         'title': 'Добавить пост',
#         'menu': menu,
#         'flag_post': 'post',
#         'form': form,
#     }
#     return render(request, 'forum/add_post.html', context=context)
