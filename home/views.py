from django.shortcuts import render
from blog.models import BlogPost
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    blogs = BlogPost.objects.order_by('-pub_date')[:20]
    authors = list(set([b.author() for b in blogs][::-1]))
    if request.user.is_authenticated:
        return render(request, 'home/index.html', {'user': request.user, 'blogs' : blogs, 'authors' : authors})
    else:
        return render(request, 'home/index.html', {'user': None, 'blogs' : blogs, 'authors' : authors})
