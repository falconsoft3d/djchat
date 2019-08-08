from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth import logout, login

# Create your views here.

@login_required(login_url="/dashboard/login")
def index_dashboard(request):
    return render(request, "dashboard.html")

def login_user(request):
    return render(request, "login.html")

@login_required(login_url="/dashboard/home")
def dashboard_home(request):
    return render(request, "home.html")

def dashboard_register(request):
    return render(request, "register.html")

def auth(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/dashboard')
    else:
        return redirect('/dashboard/login')
        
    # import pdb;pdb.set_trace()

def logout_user(request): 
    logout(request)
    return redirect('/dashboard/login')
    
    
