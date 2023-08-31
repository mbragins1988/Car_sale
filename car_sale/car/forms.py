from django.forms import DateTimeInput, ModelForm, Textarea, TextInput
from django.core.exceptions import ValidationError

from car.models import *


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
