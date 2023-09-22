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
from forum.utils import menu


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


# class CarDeleteView(DeleteView):
#     model = Car
#     template_name = 'car/delete_car.html'
#     context_object_name = 'car'
#     success_url = '/car/'


def index(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': 'Объявления',
        'cars': cars,
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
        'title': 'Добавление автомобиля',
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


def login(request):
    context = {
        'title': 'Регистрация',
        'menu': menu,
        'flag_car': 'car',
    }
    return render(request, 'register/login.html', context=context)

def category(request, cat_slug):
    cars=Car.objects.filter(cat__slug=cat_slug)
    context = {
        'title': 'Категории',
        'menu': menu,
        'cars': cars,
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
