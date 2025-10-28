from django.urls import path, re_path
from . import views

urlpatterns = [
    path('home/', views.home, name='home_page'),
    path('post/', views.post, name='post'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    re_path(r'^archive/(?P<year>[0-9]{4})/$', views.year_archive),
]
