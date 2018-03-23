from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from blog.models import BlogPost

# Create your views here.

def index(request):
    return render(request, 'blog/index.html', {'blog' : None})

def save_blog(request):
    blog_title = request.POST.get('blog_title', None)
    blog_text = request.POST.get('blog_text', None)
    blog_id = request.POST.get('blog_id', None)
    print("blog id: {0}\nblog text: {1}".format(blog_id, blog_text))
    if blog_id is not None:
        blog_post = get_object_or_404(BlogPost, pk=blog_id)
        blog_post.blog_title = blog_title
        blog_post.blog_text = blog_text
        blog_post.pub_date = timezone.now()
        print(blog_post)
        blog_post.save()
    else:
        blog_post = BlogPost(blog_title=blog_title, blog_text=blog_text, pub_date=timezone.now(), blog_author=request.user)
        print(blog_post)
        blog_post.save()
    return redirect('/')

def edit(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, 'blog/index.html', {'blog' : blog})

def delete(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    blog.delete()
    return redirect('/')

