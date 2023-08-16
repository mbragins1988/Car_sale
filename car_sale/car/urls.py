from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('add/', add, name='add'),
    path('<int:pk>', CarView.as_view(), name='detail_car'),
    path('<int:pk>/update', CarUpdateView.as_view(), name='update_car'),
    path('<int:pk>/delete', CarDeleteView.as_view(), name='delete_car'),
]
