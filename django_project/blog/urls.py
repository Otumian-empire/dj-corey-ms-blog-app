from django.urls import path, include

# from .models import *
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
]
