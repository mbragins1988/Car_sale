from django.urls import path
from django.views.decorators.cache import cache_page

from forum.views import *

app_name = 'forum'

urlpatterns = [
    path('', cache_page(60)(ForumHome.as_view()), name='forum'),
    path('category/<slug:cat_slug>', cache_page(60)(PostCategory.as_view()), name='category'),
    path('post/<slug:post_slug>', cache_page(60)(PostDetail.as_view()), name='post_detail'),
    path('add_post', AddPost.as_view(), name='add_post'),
    path('feedback', FeedbackFormView.as_view(), name='feedback'),
]
