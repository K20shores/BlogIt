from django.shortcuts import render
from blog.models import BlogPost

# Create your views here.

def index(request):
    blogs = BlogPost.objects.order_by('-pub_date')[:20]
    print(len(blogs))
    if request.user.is_authenticated:
        return render(request, 'home/index.html', {'user': request.user, 'blogs' : blogs})
    else:
        return render(request, 'home/index.html', {'user': None, 'blogs' : blogs})
