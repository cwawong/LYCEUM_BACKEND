# Create your views here.
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='posts'),
    path('post/<str:pk>/', views.PostDetail.as_view(), name='post'),
    path('users/', views.UserList.as_view(), name='users'),
    path('user/<str:pk>/', views.UserDetail.as_view(), name='user'),
    path('sub-posts/', views.SubPostList.as_view(), name='sub-posts'),
    path('sub-post/<str:pk>/', views.SubPostDetail.as_view(), name='sub-post'),
    path('tags/', views.TagList.as_view(), name='tags'),
    path('tag/<str:pk>/', views.TagDetail.as_view(), name='tag')
]
