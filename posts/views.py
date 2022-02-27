from django.shortcuts import render
from .models import Post
from .RPimqttconnect import run
from .DMS import rec


def home(request):
    context = {
        'posts': Post.objects.all(),
        'sensor_data': run(),
        'output1': rec(1),
        'output2': rec(2),
        'output3': rec(3),
        'output4': rec(4),
        'output5': rec(5),
    }
    return render(request, 'posts/home.html', context)


def social(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts/social.html', context)


def live(request):
    context = {
        'sensor_data': run()
    }
    return render(request, 'posts/live.html', context)


def recommendation(request):
    context = {
        'output1': rec(1),
        'output2': rec(2),
        'output3': rec(3),
        'output4': rec(4),
    }

    return render(request, 'posts/recommendation.html', context)


def capacity(request):
    context = {
    }
    return render(request, 'posts/capacity.html', context)


from twilio.rest import Client

account_sid = "AC1faeb5a17a707334c4167c42d28bbe9d"
auth_token = '92356264b9e6ef6b88178a500feb8e42'
client = Client(account_sid, auth_token)
message = client.messages.create(
    body=rec(4),
    from_="+18507559843",
    to="+16138063817")
message.sid
