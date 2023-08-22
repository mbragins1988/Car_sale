from django.contrib import admin
from car.models import *


class CarAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Car, CarAdmin)
admin.site.register(Category_car, CarAdmin)
