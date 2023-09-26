from django.contrib import admin
from car.models import *


class CarAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'slug', 'brand', 'model', 'time_create', 'price', 'is_published'
        )
    list_display_links = ('id', 'brand', 'model')
    search_fields = ('brand', 'price ')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('brand',)}

class Category_carAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Car, CarAdmin)
admin.site.register(Category_car, Category_carAdmin)
