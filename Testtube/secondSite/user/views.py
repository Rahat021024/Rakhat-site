from django.shortcuts import render
from .models import *

def index(request):
  return render(request, 'user/index.html', name='home')