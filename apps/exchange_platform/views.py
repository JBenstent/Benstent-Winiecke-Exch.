from django.shortcuts import render, reverse, HttpResponse
from django.contrib import messages
from . models import *

def index(request):
    print("*"*50)
    return render(request, 'exchange_platform/index.html')

def baseball(request):
    return render(request, 'exchange_platform/baseball.html')
