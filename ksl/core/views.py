from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. Welcome to the main page.")

def detail(request):
    return HttpResponse("Hello user, welcome to a different page.")
