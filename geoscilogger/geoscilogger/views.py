from django.shortcuts import render
from .models import post
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')