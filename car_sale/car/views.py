from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.cache import cache_page

from car.forms import *
from car.models import *
from forum.utils import *


def detail_car(request, car_slug):
    car = get_object_or_404(Car, slug=car_slug)
    context = {
        'title': 'объявление',
        'menu': menu,
        'car': car,
        'cat_selected': car.cat_id,
        'flag_car': 'car',
    }
    return render(request, 'car/detail_car.html', context=context)


@cache_page(60) 
def index(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Объявления',
        'page_obj': page_obj,
        'menu': menu,
        'cat_selected': 0,
        'flag_car': 'car',
    }
    return render(request, 'car/index.html', context=context)


def about(request):
    context = {
        'title': 'Что такое CarSale',
        'menu': menu,
        'flag_car': 'car',
    }
    return render(request, 'car/about.html', context=context)


@login_required
def add(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car:home')
    else:
        form = CarForm()
        
    context = {
        'title': 'Добавить автомобиль',
        'form': form,
        'menu': menu,
        'flag_car': 'car',
    }
    return render(request, 'car/add.html', context=context)


def contacts(request):
    context = {
        'title': 'Контакты',
        'menu': menu,
        'flag_car': 'car',
    }
    return render(request, 'car/contacts.html', context=context)


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'register/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('car:home')
    
def logout_user(request):
    logout(request)
    return redirect('car:login')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register/register.html'
    success_url = reverse_lazy('car:login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('car:home')

@cache_page(60)
def category(request, cat_slug):
    cars = Car.objects.filter(cat__slug=cat_slug)
    paginator = Paginator(cars, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Категории',
        'menu': menu,
        'page_obj': page_obj,
        'cat_selected': cat_slug,
        'flag_car': 'car',
    }
    return render(request, 'car/index.html', context=context)

def page_not_found(request, exception):
    return render(request, 'errors/404.html', {'path': request.path}, status=404)

def permission_denied(request, exception):
    return render(request, 'errors/403.html', status=403)

def server_error(request):
    return render(request, 'errors/500.html', status=500)
