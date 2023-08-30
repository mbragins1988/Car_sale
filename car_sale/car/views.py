from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


from car.forms import *
from car.models import *

menu = [
    {'title': 'Объявления', 'url_name': 'car:home'},
    {'title': 'Форум', 'url_name': 'forum:forum'},
    {'title': 'О сайте', 'url_name': 'car:about'},
    {'title': 'Обратная связь', 'url_name': 'car:contacts'},
    {'title': 'Контакты', 'url_name': 'car:contacts'},
    {'title': 'Войти', 'url_name': 'car:login'},
    ]

# class CarUpdateView(UpdateView):
#     model = Car
#     template_name = 'car/add.html'
#     context_object_name = 'car'

#     form_class = CarForm 


def detail_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    context = {
        'title': 'объявление',
        'menu': menu,
        'car': car,
    }
    return render(request, 'car/detail_car.html', context=context)

# class CarView(DetailView):
#     model = Car
#     template_name = 'car/detail_car.html'
#     context_object_name = 'car'


# class CarDeleteView(DeleteView):
#     model = Car
#     template_name = 'car/delete_car.html'
#     context_object_name = 'car'
#     success_url = '/car/'


def index(request):
    cars = Car.objects.all()
    context = {
        'title': 'Объявления',
        'cars': cars,
        'menu': menu,
        'cat_selected': 0
    }
    return render(request, 'car/index.html', context=context)


def about(request):
    context = {
        'title': 'Что такое CarSale',
        'menu': menu,
    }
    return render(request, 'car/about.html', context=context)

def add(request):
    error = ''
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('car:home')
        else:
            error = 'Неправильно введены данные'
    form = CarForm
    context = {
        'title': 'Добавление автомобиля',
        'form': form,
        'error': error,
        'menu': menu,
    }
    return render(request, 'car/add.html', context=context)


def contacts(request):
    context = {
        'title': 'Контакты',
        'menu': menu,
    }
    return render(request, 'car/contacts.html', context=context)

def login(request):
    context = {
        'title': 'Регистрация',
        'menu': menu,
    }
    return render(request, 'register/login.html', context=context)

def category(request, cat_id):
    cars=Car.objects.filter(cat=cat_id)
    context = {
        'title': 'Категории',
        'menu': menu,
        'cars': cars,
        'cat_selected': cat_id,
    }
    return render(request, 'car/index.html', context=context)

def page_not_found(request, exception):
    return render(request, 'errors/404.html', {'path': request.path}, status=404)

def permission_denied(request, exception):
    return render(request, 'errors/403.html', status=403)

def server_error(request):
    return render(request, 'errors/500.html', status=500)
