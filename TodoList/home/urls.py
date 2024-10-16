"""TodoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.handlelogin, name='handlelogin'),
    path('signup', views.handlesignup, name='handlesignup'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('index', views.home, name='home'),
    path('tasks', views.tasks, name='tasks'),
    path('delete/<task_id>', views.delete, name='delete'),
    path('complete/<task_id>', views.complete, name='complete'),
    path('pending/<task_id>', views.pending, name='pending'),
    path('contact', views.contact, name='contact'),
]
