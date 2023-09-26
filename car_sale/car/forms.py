from car.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import (CharField, DateTimeInput, EmailField, EmailInput,
                          ModelForm, PasswordInput, Textarea, TextInput)


class CarForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Car
        fields = (
            'brand', 'model', 'slug', 'date', 'price', 'number_owners', 'text', 'photo', 'cat'
        )

        widgets = {
            'brand': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Марка автомобиля',
            }),
            'model': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Модель автомобиля',
            }),
            'slug': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cлаг',
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год выпуска',
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена',
            }),
            'number_owners': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество владельцев',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание',
            }),
        }

    def clean_brand(self):
        brand = self.cleaned_data['brand']
        if len(brand) > 100:
            raise ValidationError('Длина превышает допустимую')
        return brand


class RegisterUserForm(UserCreationForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}))
    email = EmailField(label='Email', widget=EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))
    password2 = CharField(label='Повтор пароля', widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторите пароль'}))
 
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class LoginUserForm(AuthenticationForm):
    username = CharField(label='Логин', widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}))
 
    class Meta:
        model = User
        fields = ("username", "password")