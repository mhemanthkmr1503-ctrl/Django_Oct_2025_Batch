from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from .views import PostView
from . import views

urlpatterns = [
    path('home/', views.home, name='home_page'),
    path('posts/', PostView.as_view(), name='post'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('attendance/', views.attendance, name='attendance'),
    path('accounts/login/', auth_views.LoginView.as_view() , name='login'),
    path('register/', views.register , name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('change_password/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    re_path(r'^archive/(?P<year>[0-9]{4})/$', views.year_archive),
]
