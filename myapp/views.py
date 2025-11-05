from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from datetime import datetime
from .form import LoginForm, AttendanceForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# Home
# About
# Contact

def home(request):
    return render(request, 'home.html')

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

def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form' : form})

def attendance(request):
    if request.method == 'GET':
        print("GET Method")
        form = AttendanceForm()
        return render(request, 'attendance_form.html', {'form' : form})
    elif request.method == 'POST':
        print("POST Method")
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Thanks for Submitting Your Attendance')
        # name = request.POST.get('name', '')
        # student_id = request.POST.get('student_id', '')
        # print(name)
        return render(request, 'attendance_form.html', {'form' : form})        # print(student_id)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})