from django.shortcuts import render
from django.contrib.auth.models import User
from django.core import serializers
from blog.models import BlogPost

# Create your views here.

def index(request):
    blogs = BlogPost.objects.order_by('-pub_date')
    authors = list(set([b.blog_author for b in blogs][::-1]))
    authors = [{'name' : author, 'value' : author.lower()} for author in authors]
    props = {'blogs' : make_blogs_array(blogs), 'authors' : authors}
    user = None
    if request.user.is_authenticated:
        user = request.user
    return render(request, 'home/index.html', {'user': user, 'component' : "js/bundle.js", 'props' : props})

def make_blogs_array(blogs):
    b = []
    for blog in blogs:
        b.append({'blog_title' : blog.blog_title,
         'blog_author' : blog.blog_author,
         'blog_text' : blog.blog_text,
         'pub_date' : blog.pub_date.strftime("%Y-%m-%d %H:%M:%S"),
         'class' : blog.blog_author.lower() + " blog",
        })
    return b
