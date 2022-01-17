from django.shortcuts import render
from .models import Post
from .RPimqttconnect import run

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/home.html', context)


def live(request):
    context = {
        'sensor_data': run()
    }
    return render(request, 'posts/live.html', context)
