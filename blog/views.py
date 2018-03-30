from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.utils import timezone

from blog.models import BlogPost

# Create your views here.

def index(request):
    return render(request, 'blog/index.html', {'blog' : None})

def save_blog(request):
    blog_title = request.POST.get('blog_title', None)
    blog_text = request.POST.get('blog_text', None)
    blog_id = request.POST.get('blog_id', None)
    if blog_id is not None:
        blog_post = get_object_or_404(BlogPost, pk=blog_id)
        blog_post.blog_title = blog_title
        blog_post.blog_text = blog_text
        blog_post.pub_date = timezone.now()
        blog_post.save()
    else:
        blog_post = BlogPost(blog_title=blog_title, blog_text=blog_text, pub_date=timezone.now(), blog_author=request.user.username, blog_author_user=request.user)
        blog_post.save()
    return redirect('/')

def edit(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, 'blog/index.html', {'blog' : blog})

def delete(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    blog.delete()
    return redirect('/')

def get_blogs(request):
    props = get_blog_data()
    if request.user.is_authenticated:
        props['logged_in'] = request.user.username
    else:
        props['logged_in'] = None
    return JsonResponse(props)

def get_blog_data():
    blogs = make_blogs_array(BlogPost.objects.order_by('-pub_date'))
    authors = list(set([b['blog_author'] for b in blogs][::-1]))
    authors = [{'name' : author, 'value' : author.lower()} for author in authors]
    return {'blogs' : blogs, 'authors' : authors}

def make_blogs_array(blogs):
    b = []
    for blog in blogs:
        b.append({'blog_title' : blog.blog_title,
         'blog_author' : blog.blog_author,
         'blog_text' : blog.blog_text,
         'pub_date' : blog.pub_date.strftime("%Y-%m-%d %H:%M:%S"),
         'class' : blog.blog_author.lower(),
         'id' : blog.pk
        })
    return b
