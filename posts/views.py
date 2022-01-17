from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/home.html', context)


def live(request):
    context = {
        'sensor_data': '20 degrees'
    }
    return render(request, 'posts/live.html', context)
