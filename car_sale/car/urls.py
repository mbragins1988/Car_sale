from django.urls import path

from car.views import *

app_name = 'car'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('add/', add, name='add'),
    path('<int:car_id>', detail_car, name='detail_car'),
    path('<int:cat_id>', category, name='category'),
    # path('/<int:pk>/', CarView.as_view(), name='detail_car'),
    # path('<int:pk>/update', CarUpdateView.as_view(), name='update_car'),
    # path('<int:pk>/delete', CarDeleteView.as_view(), name='delete_car'),
    path('login/', login, name='login'),
]
