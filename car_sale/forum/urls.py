from django.urls import path

from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', forum, name='forum'),
]