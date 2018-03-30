from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save_blog', views.save_blog, name='save_blog'),
    path('edit/<int:blog_id>', views.edit, name='edit'),
    path('delete/<int:blog_id>', views.delete, name='delete'),
    path('get_blogs', views.get_blogs, name='get_blogs'),
]
