from django.shortcuts import render

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'home/index.html', {'user': request.user})
    else:
        return render(request, 'home/index.html', {'user': None})
