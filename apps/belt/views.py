from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from datetime import datetime
from ..login.models import User

def home(request):
    context = {
        'first_name': request.session['first_name']
    }
    print(request.session['first_name'])
    return render(request, 'belt/index.html', context)
