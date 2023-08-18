from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DeleteView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


from car.forms import *
from car.models import *


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car/add.html'
    context_object_name = 'car'

    form_class = CarForm 


class CarView(DetailView):
    model = Car
    template_name = 'car/detail_car.html'
    context_object_name = 'car'


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car/delete_car.html'
    context_object_name = 'car'
    success_url = '/car/'


def index(request):
    cars = Car.objects.all()
    context = {
        'title': 'Объявления',
        'cars': cars,
    }
    return render(request, 'car/index.html', context)


def about(request):
    context = {
        'title': 'Что такое CarSale'
    }
    return render(request, 'car/about.html', context)

def add(request):
    error = ''
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
        else:
            error = 'Неправильно введены данные'
    form = CarForm
    context = {
        'title': 'Добавление автомобиля',
        'form': form,
        'error': error,
    }
    return render(request, 'car/add.html', context)


def contacts(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'car/contacts.html', context)


def page_not_found(request, exception):
    return render(request, 'errors/404.html', {'path': request.path}, status=404)

def permission_denied(request, exception):
    return render(request, 'errors/403.html', status=403)

def server_error(request):
    return render(request, 'errors/500.html', status=500)