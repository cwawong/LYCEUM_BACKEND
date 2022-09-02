

# Create your views here.
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('getPosts/', views.getPosts, name='posts'),
    path('getPost/<str:pk>/', views.getPost, name='posts')
]