from django.shortcuts import render
from .models import *

def index(request):
    news = Danatube.objects.all()
    return render(request, 'main/index.html', {'news': news})

def user(request):
    return render(request, 'main/user.html')

# Create your views here.
