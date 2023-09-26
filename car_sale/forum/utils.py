from forum.models import *
from django.db.models import Count

menu = [
    {'title': 'Объявления', 'url_name': 'car:home'},
    {'title': 'Форум', 'url_name': 'forum:forum'},
    {'title': 'О сайте', 'url_name': 'car:about'},
    {'title': 'Обратная связь', 'url_name': 'forum:feedback'},
    {'title': 'Контакты', 'url_name': 'car:contacts'},
    ]


class DataMixin:
    paginate_by = 10

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category_forum.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context