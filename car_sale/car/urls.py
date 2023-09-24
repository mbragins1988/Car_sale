from django.urls import path

from car.views import *

app_name = 'car'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('add/', add, name='add'),
    path('<slug:car_slug>', detail_car, name='detail_car'),
    path('cat/<slug:cat_slug>', category, name='category'),
    # path('<int:pk>/update', CarUpdateView.as_view(), name='update_car'),
    # path('<int:pk>/delete', CarDeleteView.as_view(), name='delete_car'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]
