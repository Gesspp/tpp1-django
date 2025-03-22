from django.shortcuts import render
from .models import Greeting


def hello(request, name):
    Greeting(name=name).save()
    return render(request, 'hello.html', {'name': name})

def stats(request):
    count_greetings = Greeting.objects.count()
    return render(request, 'stats.html', {'count_greetings': count_greetings})

def ststs(request, name):
    greetings = Greeting.objects.filter(name=name)
    return render(request, 'ststs.html', {'greetings': greetings, 'name': name})

# def index(request):
#     return render(request, 'index.html')
