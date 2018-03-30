from django.shortcuts import render
from django.contrib.auth.models import User
from django.core import serializers
from blog.models import BlogPost
from blog.views import get_blog_data

# Create your views here.

def index(request):
    props = get_blog_data()
    user = None
    if request.user.is_authenticated:
        user = request.user
        props['logged_in'] = user.username
    else:
        props['logged_in'] = None
    return render(request, 'home/index.html', {'user': user, 'component' : "js/bundle.js", 'props' : props})

