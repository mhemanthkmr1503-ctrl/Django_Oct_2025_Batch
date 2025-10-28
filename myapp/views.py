from django.shortcuts import render
from django.http import HttpResponse, request
from datetime import datetime
# Create your views here.

# Home
# About
# Contact

def home(request):
    return HttpResponse("Home Page")

def about(request):
    title = "About Us"
    team_members = 24

    context = {
        'title' : title,
        'team_size' : team_members
    }

    return render(request, 'about.html', context)

def post(request):

    posts = [
        {
            "title" : "Test1",
            "created_at" : datetime(2024,12,24)
        },
        {
            "title" : "Test2",
            "created_at" : datetime(2024,12,24)
        }
    ]

    context = {
        'posts' : []
    }

    return render(request, 'post.html', context)

def year_archive(request, year):
    return HttpResponse("Year :" + str(year))

def contact(request):

    context = {
        'contact' : "+91-9876543215"
    }

    return render(request, 'contact.html', context)