from django import forms 
from forum.models import *
from django.core.exceptions import ValidationError


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Forum
        fields = ('title', 'slug', 'text', 'photo', 'cat')

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема',
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Слаг',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание',
            }),
            
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 100:
            raise ValidationError('Длина превышает допустимую')
        return title
