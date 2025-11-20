from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from .views import PostView, PostDetailedView, PostCreateView, PostUpdateView, PostDeleteView, AttendanceFormView
from . import views

urlpatterns = [
    path('home/', views.home, name='home_page'),
    path('posts/', views.post, name='post'),
    path('posts/<int:id>', PostDetailedView.as_view(), name='post_details'),
    path('posts/create', PostCreateView.as_view(), name='create_post'),
    path('success/', views.success, name='success'),
    path('posts/update/<int:id>', PostUpdateView.as_view(), name='update_post'),
    path('posts/delete/<int:id>', PostDeleteView.as_view(), name='delete_post'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('attendance/', views.attendance, name='attendance'),
    path('attendance/post', AttendanceFormView.as_view(), name='attendance'),
    path('accounts/login/', auth_views.LoginView.as_view() , name='login'),
    path('register/', views.register , name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('change_password/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    re_path(r'^archive/(?P<year>[0-9]{4})/$', views.year_archive),
]
