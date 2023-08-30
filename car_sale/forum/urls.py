from django.urls import path

from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', forum, name='forum'),
    path('category/<slug:cat_slug>', category, name='category'),
    path('post/<slug:post_slug>', post_detail, name='post_detail'),
]
