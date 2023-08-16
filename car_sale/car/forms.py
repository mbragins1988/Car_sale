from django.forms import DateTimeInput, ModelForm, Textarea, TextInput

from car.models import *


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = (
            'brand', 'model', 'date', 'price', 'number_owners', 'text', 'photo'
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
            'photo': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество владельцев',
            }),
        }
