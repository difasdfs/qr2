from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group

from .decorators import unauthenticated_user

# Create your views here.
def index(request):
    # UNTUK NGEBEDAIN GRUPNYA
    return render(request, 'index.html')

def halaman_login(request):
    context = {}

    if request.method == 'POST':
        uname = request. 

    return render(request, 'halaman_login.html', context)

# Backoffice
def index_backoffice(request):
    return render(request, 'backoffice/index.html')

# MEMBER