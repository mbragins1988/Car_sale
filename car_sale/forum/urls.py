from django.urls import path
from django.views.decorators.cache import cache_page
from forum.views import *

app_name = 'forum'

urlpatterns = [
    # path('', cache_page(60)(ForumHome.as_view()), name='forum'),
    path('', ForumHome.as_view(), name='forum'),
    path('category/<slug:cat_slug>', PostCategory.as_view(), name='category'),
    path('<slug:post_slug>', PostDetail.as_view(), name='post_detail'),
    path('<slug:post_slug>/update', ForumUpdateView.as_view(), name='post_update'),
    path('post/<slug:post_slug>/delete', ForumDeleteView.as_view(), name='post_delete'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('feedback/', FeedbackFormView.as_view(), name='feedback'),
]
