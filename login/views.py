from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def index(request):
    return render(request, 'login/index.html', {})

def blog_authenticate(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'login/index.html', {'error_message' : "Invalid credentials, try again."})

def create_account(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    password_verification = request.POST.get('password_verification', None)
    if (password != password_verification):
        return render(request, 'login/index.html', {'error_message' : "The passwords do not match. Please re-enter them."})
    else:
        user = User.objects.create_user(username=username, password=password)
        return redirect('/')

def blog_logout(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        print("error, user is not authenticated")
    return redirect('/')

