from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.events, name='events'),
    path('hello/', views.hello, name="Hello World")
]
