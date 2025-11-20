from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, request
from datetime import datetime
from .form import LoginForm, AttendanceForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import Post, Attendance
from django.db.models import Avg, Count, Min, Max, Sum

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

    result = Attendance.objects.values('name').annotate(attendance_count=Count('student_id'))

    print(result)

    return render(request, 'post.html', context)

class PostView(ListView):
    model = Post
    template_name = "post.html"
    context_object_name = "posts"

class PostDetailedView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"
    pk_url_kwarg = 'id'

class PostCreateView(CreateView):
    model = Post
    template_name = "create_post.html"
    context_object_name = "form"
    fields = ['title', 'content', 'author', 'cover_image']
    success_url='/success'

class PostUpdateView(UpdateView):
    model = Post
    template_name = "create_post.html"
    context_object_name = "form"
    fields = ['title', 'content', 'author']
    pk_url_kwarg = 'id'
    success_url='/success'

class PostDeleteView(DeleteView):
    model = Post
    pk_url_kwarg = 'id'
    success_url='/success'

    def get(self, request, *args, **kwargs):
        # Skip the confirmation page, delete directly
        self.object = self.get_object()
        self.object.delete()
        return redirect('/success')

class AttendanceFormView(FormView):
    form_class = AttendanceForm
    template_name = "create_post.html"
    context_object_name = "form"

def success(request):
    return render(request, 'success.html')

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


@permission_required('myapp.add_attendance')
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