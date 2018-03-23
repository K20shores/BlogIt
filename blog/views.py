from django.shortcuts import render, redirect
from django.utils import timezone

from blog.models import BlogPost

# Create your views here.

def index(request):
    return render(request, 'blog/index.html', {})

def create(request):
    blog_title = request.POST.get('blog_title', None)
    blog_text = request.POST.get('blog_text', None)
    blog_post = BlogPost(blog_title=blog_title, blog_text=blog_text, pub_date=timezone.now(), blog_author=request.user)
    print(blog_post)
    blog_post.save()
    return redirect('/')
