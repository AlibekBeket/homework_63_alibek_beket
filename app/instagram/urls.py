from django.urls import path

from instagram.views.posts import PostsListView

urlpatterns = [
    path('', PostsListView.as_view(), name='posts_list'),
]
