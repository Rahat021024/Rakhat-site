from django.shortcuts import render
from .models import *

def index(request):
    news = Danatube.objects.all()
    return render(request, 'main/index.html', {'news': news})

def user(request):
    person = Danatube.objects.all()
    return render(request, 'main/user.html', {"person": person})

def history(request):
    person = Danatube.objects.all()
    return render(request, 'main/history.html', {"person": person})

# Create your views here.
