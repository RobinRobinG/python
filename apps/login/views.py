from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
from datetime import datetime

def index(request):
    return render(request, 'login/login.html')

def login(request):
    if request.method=="POST":
        user = User.objects.loginValidation(request.POST)
        if isinstance(user, list):
            for error in user:
                messages.add_message(request, messages.INFO, error, extra_tags="login")
            return redirect('login:index')
        else:
            set_user_session(request,user)
            return redirect('login:success')
    return redirect('login:index')

def register(request):
    if request.method=="POST":
        user = User.objects.registerValidation(request.POST)
        if isinstance(user, list):
            for error in user:
                messages.add_message(request, messages.INFO, error, extra_tags="reg")
            return redirect('login:index')
        else:
            set_user_session(request,user)
            return redirect('login:success')
    return redirect('login:index')

def success(request):
    context = {
        'first_name': request.session['first_name']
    }
    #return redirect('login:new_page')
    return render(request, 'login/success.html', context)


def logout(request):
    request.session.clear()
    return redirect('login:index')

def set_user_session(request,user):
    request.session['user_id'] = user.id
    request.session['first_name'] = user.first_name