from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/home.html', context)


def live(request):
    return render(request, 'posts/live.html', {'title': 'Live'})
