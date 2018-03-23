from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog_authenticate', views.blog_authenticate, name='blog_authenticate'),
    path('create_account', views.create_account, name='create_account'),
    path('blog_logout', views.blog_logout, name='blog_logout'),
]

