from django.urls import path

from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', forum, name='forum'),
    path('<int:cat_id>', category, name='category'),
    path('<int:post_id>', post_detail, name='post_detail'),
]
