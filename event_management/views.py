from django.shortcuts import render
from django.http import HttpResponse

def events(request):
    return HttpResponse("Hello world!")

def hello(request):
    return HttpResponse("Testing Hello World!")