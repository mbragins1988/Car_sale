from django.urls import path

from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', ForumHome.as_view(), name='forum'),
    path('category/<slug:cat_slug>', PostCategory.as_view(), name='category'),
    path('post/<slug:post_slug>', PostDetail.as_view(), name='post_detail'),
    path('add_post', AddPost.as_view(), name='add_post'),
]
