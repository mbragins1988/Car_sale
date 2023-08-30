from django import template
from car.models import *
from forum.models import *

register = template.Library()

@register.inclusion_tag('forum/show_category.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category_forum.objects.all()
    else:
        cats = Category_forum.objects.order_by(sort)
    
    return {'cats': cats, 'cat_selected': cat_selected}

@register.inclusion_tag('car/categories_car.html')
def categories_car(sort=None, cat_selected=0):
    if not sort:
        cats = Category_car.objects.all()
    else:
        cats= Category_car.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}

@register.inclusion_tag('menu.html')
def menu(menu):
    return {'menu': menu}
