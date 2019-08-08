from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth import logout, login

# Public
def login_user(request):
    return render(request, "login.html")

def dashboard_register(request):
    return render(request, "register.html")


# Private
@login_required(login_url="/dashboard/login")
def index_dashboard(request):
    return render(request, "dashboard.html")

@login_required(login_url="/dashboard/login")
def change_password(request):
    return render(request, "change_password.html")

@login_required(login_url="/dashboard/home")
def dashboard_visitors(request):
    return render(request, "visitors.html")

@login_required(login_url="/dashboard/profile")
def dashboard_profile(request):
    return render(request, "profile.html")

@login_required(login_url="/dashboard/profile")
def dashboard_widget(request):
    return render(request, "widget.html")

@login_required(login_url="/dashboard/home")
def dashboard_record(request):
    return render(request, "record.html")

@login_required(login_url="/dashboard/home")
def dashboard_home(request):
    return render(request, "home.html")

def auth(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/dashboard/home')
    else:
        return redirect('/dashboard/login')
        
    # import pdb;pdb.set_trace()

def logout_user(request): 
    logout(request)
    return redirect('/dashboard/login')
    
    
